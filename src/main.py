from typing import Final

from dotenv import load_dotenv

from cv2.typing import MatLike

from load.image_load import load_images_from_dir
from view.view_image import show_image

PNG_IMAGES_DIR: Final[str] = "images"

if __name__ == "__main__":
    load_dotenv()
    images: list[MatLike] = load_images_from_dir(PNG_IMAGES_DIR)
    for image in images:
        show_image(image)
