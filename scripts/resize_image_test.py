from pathlib import Path
from PIL import Image

source = Path("images/characters/kuro/kuro_happy_neon_cafe.png")
target = Path("images/characters/kuro/kuro_happy_neon_cafe_resized_test.png")

with Image.open(source) as im:
    im = im.convert("RGBA") if "A" in im.getbands() else im.convert("RGB")
    original_size = im.size
    im.thumbnail((1024, 1024), Image.Resampling.LANCZOS)
    im.save(target, format="PNG", optimize=True)
    print(f"Original dimensions: {original_size[0]}x{original_size[1]}")
    print(f"Resized dimensions: {im.width}x{im.height}")
    print(f"Original bytes: {source.stat().st_size}")
    print(f"Resized bytes: {target.stat().st_size}")
