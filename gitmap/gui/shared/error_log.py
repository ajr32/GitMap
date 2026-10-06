"""Persistent diagnostic error logging for GitMap."""

import logging
from pathlib import Path

_logger = logging.getLogger("gitmap.errors")
_logger.setLevel(logging.ERROR)
_logger.propagate = False


def _log_path(log_directory=None):
    if log_directory is not None:
        return Path(log_directory) / "errors.log"

    return Path(".gitmap") / "logs" / "errors.log"


def _ensure_handler(log_directory=None):
    path = _log_path(log_directory)
    path.parent.mkdir(parents=True, exist_ok=True)
    resolved = str(path.resolve())

    for handler in _logger.handlers:
        if isinstance(handler, logging.FileHandler):
            if str(Path(handler.baseFilename).resolve()) == resolved:
                return

    handler = logging.FileHandler(path, mode="a", encoding="utf-8")
    handler.setLevel(logging.ERROR)
    handler.setFormatter(
        logging.Formatter(
            "%(asctime)s\n%(message)s\n"
            "------------------------------------------------------------",
            datefmt="%Y-%m-%d %H:%M:%S",
        )
    )
    _logger.addHandler(handler)


def log_exception(context, error, *, diagnostic=None, log_directory=None):
    """Append an exception and its traceback to errors.log."""
    try:
        _ensure_handler(log_directory)
        message = str(context)

        if diagnostic:
            message += f"\n{diagnostic}"

        _logger.error(
            message,
            exc_info=(type(error), error, error.__traceback__),
        )
    except Exception:
        # Logging must never hide the original application error.
        pass


def log_error(context, *, diagnostic=None, log_directory=None):
    """Append a non-exception diagnostic error to errors.log."""
    try:
        _ensure_handler(log_directory)
        message = str(context)

        if diagnostic:
            message += f"\n{diagnostic}"

        _logger.error(message)
    except Exception:
        pass
