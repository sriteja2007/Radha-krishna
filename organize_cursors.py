import shutil
from pathlib import Path
from PIL import Image

cursor_dir = Path("assets/cursor")
cursor_dir.mkdir(parents=True, exist_ok=True)

# File names
f_cur = "Peacock Feather & Peacock 3D Cursor--cursor--SweezyCursors.cur"
f_png = "Peacock Feather & Peacock 3D Cursor--cursor--SweezyCursors.png"
p_cur = "Peacock Feather & Peacock 3D Cursor--pointer--SweezyCursors.cur"
p_png = "Peacock Feather & Peacock 3D Cursor--pointer--SweezyCursors.png"

# Copy cur files
shutil.copy(f_cur, cursor_dir / "peacock_feather.cur")
shutil.copy(p_cur, cursor_dir / "peacock_pointer.cur")

# Copy & resize PNGs
shutil.copy(f_png, cursor_dir / "peacock_feather.png")
shutil.copy(p_png, cursor_dir / "peacock_pointer.png")

with Image.open(f_png) as img:
    img.resize((32, 32), Image.Resampling.LANCZOS).save(cursor_dir / "peacock_feather_32.png")
    img.resize((48, 48), Image.Resampling.LANCZOS).save(cursor_dir / "peacock_feather_48.png")

with Image.open(p_png) as img:
    img.resize((32, 32), Image.Resampling.LANCZOS).save(cursor_dir / "peacock_pointer_32.png")
    img.resize((48, 48), Image.Resampling.LANCZOS).save(cursor_dir / "peacock_pointer_48.png")

print("Cursor files successfully organized into assets/cursor/!")
