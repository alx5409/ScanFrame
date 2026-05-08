import cv2
from cv2.typing import MatLike

def show_image(image: MatLike, window_name: str = "Image") -> None:
    """Displays the given image in a window."""
    cv2.imshow(window_name, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def show_images(images: list[MatLike], window_names: list[str] | None = None) -> None:
    """Displays a list of images in separate windows."""
    if window_names is None:
        window_names = [f"Image {i+1}" for i in range(len(images))]
    for image, window_name in zip(images, window_names):
        show_image(image, window_name)