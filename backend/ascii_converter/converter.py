from PIL import Image
ASCII_CHARS = "@%#*+=-:. "
def image_to_ascii(image_path, width=100):
    image = Image.open(image_path)
    image = image.convert("L")  # Convert to grayscale
    aspect_ratio = image.height / image.width
    new_height = int(width * aspect_ratio)
    image = image.resize((width, new_height))
    pixels = image.getdata()
    ascii_str = "".join(ASCII_CHARS[pixel // 32] for pixel in pixels)
    
    ascii_art = "\n".join(
        ascii_str[i : i + width] for i in range(0, len(ascii_str), width)
    )
    return ascii_art
