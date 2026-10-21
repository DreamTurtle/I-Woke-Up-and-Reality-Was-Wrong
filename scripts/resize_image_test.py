from pathlib import Path
from PIL import Image, ImageFilter, ImageEnhance

source = Path("images/characters/kuro/kuro_happy_neon_cafe.png")
target = Path("images/characters/kuro/kuro_happy_neon_cafe_landscape_test.png")
canvas_size = (1280, 720)

with Image.open(source) as opened:
    original = opened.convert("RGBA")
    # Create a 16:9 background from the same artwork, blurred to fill the wide canvas.
    background = original.convert("RGB")
    scale = max(canvas_size[0] / background.width, canvas_size[1] / background.height)
    bg_size = (round(background.width * scale), round(background.height * scale))
    background = background.resize(bg_size, Image.Resampling.LANCZOS)
    left = (background.width - canvas_size[0]) // 2
    top = (background.height - canvas_size[1]) // 2
    background = background.crop((left, top, left + canvas_size[0], top + canvas_size[1]))
    background = background.filter(ImageFilter.GaussianBlur(28))
    background = ImageEnhance.Brightness(background).enhance(0.58)

    # Keep the entire original image visible, without cropping or distorting it.
    foreground = original.copy()
    foreground.thumbnail(canvas_size, Image.Resampling.LANCZOS)
    x = (canvas_size[0] - foreground.width) // 2
    y = (canvas_size[1] - foreground.height) // 2
    background = background.convert("RGBA")
    background.alpha_composite(foreground, (x, y))
    background.convert("RGB").save(target, format="PNG", optimize=True)

    print(f"Original dimensions: {original.width}x{original.height}")
    print(f"Landscape dimensions: {canvas_size[0]}x{canvas_size[1]}")
    print("Original artwork is fully visible; no cropping or stretching.")
    print(f"Original bytes: {source.stat().st_size}")
    print(f"Landscape test bytes: {target.stat().st_size}")
