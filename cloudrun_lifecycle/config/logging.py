"""Logging configurations.
"""
import logging


FORMAT = "%(levelname)s:\t%(name)s\t%(message)s"


def configure_logger(*, debug: bool = False) -> logging.Logger:
    # Init loggers and handlers
    app_logger = logging.getLogger(__package__.split(".")[0])
    handler = logging.StreamHandler()
    app_logger.addHandler(handler)
    # Configurations
    handler.setFormatter(logging.Formatter(FORMAT))
    app_logger.propagate = not debug
    app_logger.setLevel(logging.DEBUG if debug else logging.INFO)
    return app_logger
