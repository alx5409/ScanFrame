from typing import Final

from dotenv import load_dotenv

from load.image_load import load_images_from_dir
from view.view_image import show_images
from logger.logging_config import LoggingConfig

PNG_IMAGES_DIR: Final[str] = "images"

if __name__ == "__main__":
    LoggingConfig.configure_logging()
    load_dotenv()
    images = load_images_from_dir(PNG_IMAGES_DIR)
    show_images(images)