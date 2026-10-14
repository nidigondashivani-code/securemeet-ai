import logging
import sys
from pythonjsonlogger import jsonlogger
from app.core.config import settings


def setup_logging() -> None:
    """Configures structured JSON logging for enterprise observability."""
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG if settings.DEBUG else logging.INFO)

    log_handler = logging.StreamHandler(sys.stdout)
    formatter = jsonlogger.JsonFormatter(
        "%(asctime)s %(levelname)s %(name)s %(module)s %(lineno)d %(message)s"
    )
    log_handler.setFormatter(formatter)

    # Avoid duplicate handlers
    if not logger.handlers:
        logger.addHandler(log_handler)
    else:
        logger.handlers = [log_handler]
