# Radha–Krishna 3D Depth Map Story Website

An interactive **Three.js + WebGL Depth-Map Parallax** web experience replicating the exact workflow and visual aesthetic from the Instagram Reel.

---

## 🌐 Live Deployed Website

👉 **[https://sriteja2007.github.io/Radha-krishna/](https://sriteja2007.github.io/Radha-krishna/)**

GitHub Repository: **[https://github.com/sriteja2007/Radha-krishna](https://github.com/sriteja2007/Radha-krishna)**

---

## 📱 Laptop & Mobile Responsive Features

- **Laptop / Desktop**:
  - Interactive **3D Peacock Feather** custom cursor (`assets/cursor/peacock_feather.cur` / `.png`).
  - Morphs into **Full 3D Peacock Pointer** when hovering over interactive buttons, cards, pills, and chapter dots.
  - Ultra-smooth mouse tracking with fluid lerp inertia and idle breathing drift.

- **Mobile & Tablet**:
  - **Full Mobile Layout**: Compact frosted glass plate cards, auto-adapting typography, and responsive touch controls.
  - **Touch Gestures**: Vertical & horizontal swipe navigation between scenes, touch dragging for 3D parallax.
  - **✨ 3D Gyroscope Motion**: Tap the **"3D Tilt"** button in the header to activate phone gyro motion — physically tilting your phone tilts the scene in holographic 3D!
  - **Touchscreen Friendly**: Automatically hides desktop cursor circles to ensure clean touch rendering.

---

## 🌟 Key Highlights

1. **Depth Anything V2 Maps**:
   - 5 Radha–Krishna scenes with calibrated polarities: Subject is **WHITE** (foreground), background is **BLACK** (far depth).
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
