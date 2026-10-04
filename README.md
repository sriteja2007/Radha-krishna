# Radha–Krishna 3D Depth Map Story Website

An interactive **Three.js + WebGL Depth-Map Parallax** web experience replicating the exact workflow and visual aesthetic from the Instagram Reel.

---

## 🌟 Features Included

1. **Depth Anything V2 Maps**:
   - All 5 Radha–Krishna photos processed with Depth Anything V2 to generate pixel-accurate grayscale depth maps.
   - Strict polarity verified: Subject is **WHITE** (foreground), background is **BLACK** (far depth).

2. **Custom WebGL Parallax Shader**:
   - Fullscreen plane with aspect-ratio preserving `cover` UV coordinates.
   - Displaces each pixel's UV by `(depth − 0.45) × mouse offset × intensity`.
   - Near and far elements move in opposing directions around the `0.45` focal anchor, creating true holographic 3D depth.
   - Subtle chromatic aberration and depth-based dissolve transitions.

3. **Autonomous Idle Drift**:
   - Gentle floating breathing motion when untouched (`sin` / `cos` oscillation).

4. **Multi-Chapter Snap-Scroll Story**:
   - **Scene 1**: *The Awakening* — *"She does not remember him"*
   - **Scene 2**: *The Sacred Chandan* — *"He paints memories upon her palm"*
   - **Scene 3**: *Under the Silver Moon* — *"The sacred flute calls across time"*
   - **Scene 4**: *The Eternal Melody* — *"Closing her eyes, she awakens"*
   - **Scene 5**: *The Divine Reunion* — *"And he arrives, forever remembered"*

5. **Reel-Authentic UI**:
   - **Shrunoti: Ocean of Stories** brand badge.
   - **Google Play & App Store** download buttons.
   - **Depth View Toggle**: Switch between colored art and raw grayscale depth maps to inspect the depth mesh live.
   - **3D Intensity Slider**: Adjust the displacement depth effect in real-time.
   - **Divine Audio Engine**: Built-in Web Audio API synthesizer generating peaceful Bansuri flute notes and Tanpura drone harmonics (no external audio files needed).

---

## 🚀 How to Run

The local server is already running! Simply open:
👉 **[http://localhost:3000/](http://localhost:3000/)** in your browser.

If you ever restart your machine or wish to run it again:
```powershell
python server.py
```
Then navigate to `http://localhost:3000/`.

---

## 📁 Project Structure

- `index.html` — Complete single-file Three.js WebGL application, custom shaders, and UI.
- `server.py` — Local HTTP server with CORS and cache headers.
- `assets/`
  - `image_1.jpg` ... `image_5.jpg` — Optimized Radha–Krishna art scenes.
  - `depth_1.jpg` ... `depth_5.jpg` — Grayscale Depth Anything V2 depth maps.
- `generate_all_depth_maps.py` — Local script that generated the Depth Anything V2 models.
