from typing import Final
import os

import cv2
from cv2.typing import MatLike

ALLOWED_EXTENSIONS: Final[set[str]] = {".png", ".jpg"}

def check_path(path: str) -> None:
    """Checks if the given path exists."""
    if not os.path.exists(path):
        raise FileNotFoundError(f"Path does not exist: {path}")
    
def check_directory(directory: str) -> None:
    """Checks if the given path is a directory."""
    if not os.path.isdir(directory):
        raise NotADirectoryError(f"Path is not a directory: {directory}")
    
def get_paths_from_dir(directory: str) -> list[str]:
    """Returns a list of file paths in the specified directory that have allowed extensions."""
    check_path(directory)
    check_directory(directory)
    paths: list[str] = []
    for filename in os.listdir(directory):
        if any(filename.endswith(ext) for ext in ALLOWED_EXTENSIONS):
            paths.append(os.path.join(directory, filename))
    return paths

def load_image_from_path(image_path: str) -> MatLike:
    """Loads a PNG image from the specified path and returns it as an OpenCV image."""
    check_path(image_path)
    image = cv2.imread(image_path)
    if image is None:
        raise ValueError(f"Could not load image from path: {image_path}")
    return image

def load_images_from_dir(directory: str) -> list[MatLike]:
    """Loads all PNG images from the specified directory and returns them as a list of OpenCV images."""
    check_path(directory)
    check_directory(directory)
    paths: list[str] = get_paths_from_dir(directory)
    images: list[MatLike] = []
    for image_path in paths:
        images.append(load_image_from_path(image_path))
    return images