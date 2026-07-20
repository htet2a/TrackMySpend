import logging

from app.utils.paths import get_project_path


LOG_DIRECTORY = get_project_path("logs")


def get_logger(name: str = "TrackMySpend"):
    """
    Create and return application logger.
    """

    LOG_DIRECTORY.mkdir(exist_ok=True)

    log_file = LOG_DIRECTORY / "trackmyspend.log"

    logger = logging.getLogger(name)

    if not logger.handlers:
        logger.setLevel(logging.INFO)

        file_handler = logging.FileHandler(
            log_file,
            encoding="utf-8"
        )

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)s | %(message)s"
        )

        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)

    return logger