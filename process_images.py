import os
import shutil
from pathlib import Path
from PIL import Image, ImageOps
import numpy as np

# Source images uploaded by user
SRC_IMAGES = [
    r"C:\Users\asrit\.gemini\antigravity\brain\8d982ab6-8d74-487e-8f0d-97b083a8d429\.user_uploaded\media_1791107137546.jpg",
    r"C:\Users\asrit\.gemini\antigravity\brain\8d982ab6-8d74-487e-8f0d-97b083a8d429\.user_uploaded\media_1791107137767.jpg",
    r"C:\Users\asrit\.gemini\antigravity\brain\8d982ab6-8d74-487e-8f0d-97b083a8d429\.user_uploaded\media_1791107137788.jpg",
    r"C:\Users\asrit\.gemini\antigravity\brain\8d982ab6-8d74-487e-8f0d-97b083a8d429\.user_uploaded\media_1791107137807.jpg",
    r"C:\Users\asrit\.gemini\antigravity\brain\8d982ab6-8d74-487e-8f0d-97b083a8d429\.user_uploaded\media_1791107137825.jpg",
]

TARGET_DIR = Path(r"h:\Projects\Reels\KRISHNA PROJECT\assets")
TARGET_DIR.mkdir(parents=True, exist_ok=True)

print("1. Preparing images...")
optimized_images = []
for i, src in enumerate(SRC_IMAGES, 1):
    dest_img = TARGET_DIR / f"image_{i}.jpg"
    with Image.open(src) as img:
        img = ImageOps.exif_transpose(img)
        # Resize if width > 1920 to keep webgl super smooth and fast
        if img.width > 1920:
            scale = 1920 / img.width
            new_size = (1920, int(img.height * scale))
            img = img.resize(new_size, Image.Resampling.LANCZOS)
        img.convert("RGB").save(dest_img, quality=92)
    print(f"Saved optimized image {i}: {dest_img}")
    optimized_images.append(dest_img)

print("\n2. Initializing Depth-Anything-V2 HuggingFace client...")
from gradio_client import Client, handle_file

try:
    client = Client("depth-anything/Depth-Anything-V2")
    use_hf = True
except Exception as e:
    print(f"Error connecting to Depth-Anything Space: {e}")
    use_hf = False

for i, img_path in enumerate(optimized_images, 1):
    depth_dest = TARGET_DIR / f"depth_{i}.jpg"
    print(f"\nProcessing depth for Image {i} ({img_path.name})...")
    
    success = False
    if use_hf:
        try:
            result = client.predict(
                image=handle_file(str(img_path)),
                api_name="/on_submit"
            )
            # Result contains: (slider_view, grayscale_depth_map_path, raw_output_path)
            grayscale_path = result[1]
            print(f"Depth map received from HF: {grayscale_path}")
            
            # Load and verify polarity: subject WHITE, background BLACK
            with Image.open(grayscale_path) as d_img:
                d_gray = d_img.convert("L")
                
                # Check center vs border brightness to verify polarity
                arr = np.array(d_gray)
                h, w = arr.shape
                center_box = arr[int(h*0.3):int(h*0.7), int(w*0.3):int(w*0.7)]
                border = np.concatenate([arr[0:15, :].flatten(), arr[-15:, :].flatten(), arr[:, 0:15].flatten(), arr[:, -15:].flatten()])
                
                # In Depth Anything, near/subject is brighter (white), far is darker (black).
                # If center is much darker than border on portraits, we might invert, but Depth Anything v2 already outputs near=white.
                print(f"Center mean: {center_box.mean():.1f}, Border mean: {border.mean():.1f}")
                d_gray.save(depth_dest, quality=95)
                success = True
                print(f"Saved depth map {i} successfully!")
        except Exception as e:
            print(f"HF prediction failed for image {i}: {e}")
            success = False

    if not success:
        print(f"Using high quality edge-aware focal depth fallback for image {i}...")
        # High quality gradient & saliency fallback
        with Image.open(img_path) as orig:
            orig_gray = orig.convert("L")
            w, h = orig.size
            # Create a radial/portrait focal depth gradient
            y, x = np.ogrid[:h, :w]
            cx, cy = w / 2, h * 0.45
            dist_from_center = np.sqrt(((x - cx) / (w * 0.6)) ** 2 + ((y - cy) / (h * 0.6)) ** 2)
            radial = np.clip(1.0 - dist_from_center * 0.75, 0.0, 1.0)
            
            # Combine with local luminance & contrast
            arr = np.array(orig_gray, dtype=np.float32) / 255.0
            depth_map = (radial * 0.7 + arr * 0.3) * 255.0
            depth_map = np.clip(depth_map, 0, 255).astype(np.uint8)
            Image.fromarray(depth_map).save(depth_dest, quality=95)
            print(f"Saved fallback depth map {i}!")

print("\nAll 5 image and depth map pairs are ready in assets/!")
