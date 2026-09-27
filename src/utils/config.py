"""
src.utils.config — Configuration loading and validation.

Responsibilities:
- Load YAML config files.
- Merge multiple configs in priority order: defaults → dataset → poisoning → experiment.
- Validate required fields.
- Return typed configuration objects (dataclasses or dicts).

No parameters should be hard-coded in src/. All tunable values
come from configs/ and flow through this module.

Usage (planned):
    config = load_config("configs/default.yaml",
                         overrides=["configs/datasets/nfcorpus.yaml"])
"""

from __future__ import annotations

# TODO: Implement:
#
# def load_config(default_path: str, overrides: list[str] = None) -> dict: ...
# def merge_configs(base: dict, override: dict) -> dict: ...
# def validate_config(config: dict) -> None: ...
