import logging
from datetime import datetime
from pathlib import Path


class LoggingConfig:
    """Configures the logging settings for the application."""

    @staticmethod
    def configure_logging() -> None:
        """Configure application logging to write into logs/ with a timestamped filename."""
        logs_dir = Path("logs")
        logs_dir.mkdir(parents=True, exist_ok=True)

        timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        log_file = logs_dir / f"app_{timestamp}.log"

        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s",
            handlers=[
                logging.FileHandler(log_file, encoding="utf-8"),
                logging.StreamHandler(),
            ],
        )