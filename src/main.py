from typing import Final

import os
from dotenv import load_dotenv

import cv2
from cv2.typing import MatLike

PNG_IMAGES_DIR: Final[str] = "src/images"
ALLOWED_EXTENSIONS: Final[set[str]] = {".png", ".jpg"}

def load_image_from_path(image_path: str) -> MatLike:
    """Loads a PNG image from the specified path and returns it as an OpenCV image."""
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Could not load image from path: {image_path}")
    return image

def load_images_from_dir(directory: str) -> list[MatLike]:
    """Loads all PNG images from the specified directory and returns them as a list of OpenCV images."""
    images: list[MatLike] = []
    for filename in os.listdir(directory):
        if any(filename.endswith(ext) for ext in ALLOWED_EXTENSIONS):
            image_path = os.path.join(directory, filename)
            images.append(load_image_from_path(image_path))
    return images

if __name__ == "__main__":
    load_dotenv()
    images: list[MatLike] = load_images_from_dir(PNG_IMAGES_DIR)
    for image in images:
        cv2.imshow("Image", image)
        cv2.waitKey(0)
    cv2.destroyAllWindows()