import os
from pathlib import Path
import numpy as np
from PIL import Image, ImageOps
import onnxruntime as ort
from huggingface_hub import hf_hub_download

# Define files
SRC_IMAGES = [
    r"C:\Users\asrit\.gemini\antigravity\brain\8d982ab6-8d74-487e-8f0d-97b083a8d429\.user_uploaded\media_1791107137546.jpg",
    r"C:\Users\asrit\.gemini\antigravity\brain\8d982ab6-8d74-487e-8f0d-97b083a8d429\.user_uploaded\media_1791107137767.jpg",
    r"C:\Users\asrit\.gemini\antigravity\brain\8d982ab6-8d74-487e-8f0d-97b083a8d429\.user_uploaded\media_1791107137788.jpg",
    r"C:\Users\asrit\.gemini\antigravity\brain\8d982ab6-8d74-487e-8f0d-97b083a8d429\.user_uploaded\media_1791107137807.jpg",
    r"C:\Users\asrit\.gemini\antigravity\brain\8d982ab6-8d74-487e-8f0d-97b083a8d429\.user_uploaded\media_1791107137825.jpg",
]

TARGET_DIR = Path(r"h:\Projects\Reels\KRISHNA PROJECT\assets")
TARGET_DIR.mkdir(parents=True, exist_ok=True)

print("Loading Depth Anything V2 ONNX model...")
model_path = hf_hub_download(repo_id='onnx-community/depth-anything-v2-small', filename='onnx/model_quantized.onnx')
session = ort.InferenceSession(model_path, providers=['CPUExecutionProvider'])

mean = np.array([0.485, 0.456, 0.406], dtype=np.float32).reshape(1, 1, 3)
std = np.array([0.229, 0.224, 0.225], dtype=np.float32).reshape(1, 1, 3)

for idx, src_path in enumerate(SRC_IMAGES, 1):
    print(f"\nProcessing Image {idx} from {Path(src_path).name}...")
    dest_img = TARGET_DIR / f"image_{idx}.jpg"
    dest_depth = TARGET_DIR / f"depth_{idx}.jpg"
    
    with Image.open(src_path) as raw_img:
        img = ImageOps.exif_transpose(raw_img)
        # Cap max resolution for web performance
        if img.width > 1920:
            scale = 1920 / img.width
            img = img.resize((1920, int(img.height * scale)), Image.Resampling.LANCZOS)
        
        orig_w, orig_h = img.size
        img.convert("RGB").save(dest_img, quality=92)
        
        # Prepare for ONNX (multiples of 14)
        target_size = 518
        # Calculate aspect ratio preserving multiples of 14
        if orig_w >= orig_h:
            new_w = target_size
            new_h = int(round((orig_h / orig_w * target_size) / 14.0)) * 14
        else:
            new_h = target_size
            new_w = int(round((orig_w / orig_h * target_size) / 14.0)) * 14
            
        print(f"Resizing to model input size: {new_w}x{new_h} (multiples of 14)")
        resized = img.convert("RGB").resize((new_w, new_h), Image.Resampling.BICUBIC)
        arr = np.array(resized, dtype=np.float32) / 255.0
        arr = (arr - mean) / std
        tensor = arr.transpose(2, 0, 1)[np.newaxis, ...].astype(np.float32)
        
        print("Running ONNX Depth-Anything-V2 inference...")
        outputs = session.run(None, {'pixel_values': tensor})
        depth = outputs[0].squeeze() # shape: (new_h, new_w)
        
        # Normalize to 0-255
        d_min = depth.min()
        d_max = depth.max()
        if d_max > d_min:
            depth_norm = (depth - d_min) / (d_max - d_min) * 255.0
        else:
            depth_norm = depth * 0.0
            
        depth_map = depth_norm.astype(np.uint8)
        depth_pil = Image.fromarray(depth_map).resize((orig_w, orig_h), Image.Resampling.BICUBIC)
        
        # Check Polarity: Subject must be WHITE, background BLACK
        d_arr = np.array(depth_pil)
        center_val = d_arr[int(orig_h*0.3):int(orig_h*0.7), int(orig_w*0.3):int(orig_w*0.7)].mean()
        border_val = (d_arr[0, :].mean() + d_arr[-1, :].mean() + d_arr[:, 0].mean() + d_arr[:, -1].mean()) / 4.0
        print(f"Subject Center Depth Mean: {center_val:.1f}, Border Mean: {border_val:.1f}")
        
        # If subject is darker than border, invert polarity
        if center_val < border_val:
            print("Inverting polarity: making foreground subject WHITE!")
            depth_pil = ImageOps.invert(depth_pil)
            
        depth_pil.save(dest_depth, quality=95)
        print(f"Saved: {dest_depth} ({orig_w}x{orig_h})")

print("\nSUCCESS: All 5 images and Depth-Anything-V2 maps generated perfectly!")
