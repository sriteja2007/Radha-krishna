# Radha–Krishna 3D Depth Map Story Website

An interactive **Three.js + WebGL Depth-Map Parallax** web experience replicating the exact workflow and visual aesthetic from the Instagram Reel.

---

## 🌐 Live Deployed Website

👉 **[https://sriteja2007.github.io/Radha-krishna/](https://sriteja2007.github.io/Radha-krishna/)**

GitHub Repository: **[https://github.com/sriteja2007/Radha-krishna](https://github.com/sriteja2007/Radha-krishna)**

---

## 📱 Dual-Mode: Laptop vs Mobile Experience

The website automatically detects the user's device and loads dedicated, optimized imagery and depth maps:

### 💻 1. Laptop / Desktop Mode
- **Artwork**: 5 Landscape 16:9 Radha–Krishna art scenes.
- **Custom Cursor**: Interactive **3D Peacock Feather** cursor (`assets/cursor/peacock_feather.cur` / `.png`) with golden aura.
- **Interactive Pointer**: Morphs into the **Full 3D Peacock Pointer** when hovering over buttons, cards, pills, and chapter dots.
- **Mouse Parallax**: Smooth displacement via `(depth − 0.45) × mouse offset` with subtle harmonic idle drift when untouched.

### 📱 2. Mobile Phone & Tablet Mode
- **Artwork**: 5 Dedicated Vertical 9:16 portrait Radha–Krishna photography & art scenes tailored for smartphone screens.
- **Depth Estimation**: High-precision Depth Anything V2 depth maps calibrated specifically for vertical mobile displays.
- **✨ 3D Gyroscope Motion**: Tap the **"3D Tilt"** button in the header — physically tilting your phone tilts the scene in 3D parallax in real-time (iOS Safari & Android supported).
- **Touch Gestures**: Vertical & horizontal swipe navigation between scenes, touch dragging for 3D depth exploration.
- **Responsive Layout**: Compact frosted glass plate cards, auto-adapting typography, and responsive touch controls.
- **Touchscreen Friendly**: Desktop cursor circle automatically hidden on touch screens to ensure clean touch rendering.

---

## 🌟 Key Highlights

1. **Depth Anything V2 Depth Maps**:
   - Both Desktop and Mobile scene sets processed with Depth Anything V2: Subject is **WHITE** (foreground), background is **BLACK** (far depth).
2. **Custom WebGL Parallax Shader**:
   - Displaces each pixel's UV by `(depth − 0.45) × (mouse + drift) × intensity`.
   - Near and far elements move in opposing directions around the `0.45` focal anchor.
   - Cinematic edge chromatic aberration and aspect-ratio preserving `cover` UVs.
3. **Song & Divine Audio Support**:
   - Plays `assets/song.mp3` with a toggleable visualizer.
   - Built-in classical Indian Tanpura and Bansuri flute synthesis fallback.
4. **Interactive UI**:
   - Shrunoti branding pill, chapter selector, 3D intensity slider, and Depth Map View toggle.

---

## 💻 Local Development

Run the local server:
```powershell
python server.py
```
Open [http://localhost:3000/](http://localhost:3000/).
