import cv2
import numpy as np

ASCII_CHARS = "@%#*+=-:. "  # ASCII density mapping

def image_to_ascii(image, width=100):
    """Convert an image (numpy array) to ASCII art"""
    # Convert to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    # Resize for ASCII
    aspect_ratio = gray.shape[1] / gray.shape[0]
    new_width = width
    new_height = int(new_width / aspect_ratio * 0.55)  # Adjust height to maintain aspect ratio
    gray_resized = cv2.resize(gray, (new_width, new_height))

    # Convert pixels to ASCII
    ascii_result = "\n".join(
        "".join(ASCII_CHARS[pixel // (256 // len(ASCII_CHARS))] for pixel in row)
        for row in gray_resized
    )

    return ascii_result

