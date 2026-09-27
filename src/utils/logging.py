"""
src.utils.logging — Structured logging setup.

Configures Python's logging module with:
- Console output (human-readable, colored).
- File output (JSON lines for machine parsing).
- Configurable log level from the project config.

Usage (planned):
    from src.utils.logging import setup_logging, get_logger
    setup_logging(level="INFO", log_file="experiments/exp1/logs/run.log")
    logger = get_logger(__name__)
    logger.info("Starting Phase A", extra={"strategy": "targeted_corruption"})
"""

from __future__ import annotations

# TODO: Implement:
#
# def setup_logging(level: str = "INFO", log_file: str | None = None) -> None: ...
# def get_logger(name: str) -> logging.Logger: ...
