"""Utility script of the absolute path"""
from pathlib import Path


def absolute_path(filepath):
    """Absolute path from the relative path"""
    relative = Path(filepath)
    return relative.absolute()
