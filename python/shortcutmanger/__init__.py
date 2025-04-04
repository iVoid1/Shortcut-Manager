"""
Shortcut Manager
~~~~~~~~~~~~~~

A simple shortcut manager for Windows, Linux, and MacOS.
This package provides a simple way to create and manage shortcuts on different operating systems.
It supports creating shortcuts for files, folders, and applications, and allows you to specify custom icons and other properties.
It also provides a simple command-line interface for creating and managing shortcuts.
"""

__title__ = "shortcutmanger"
__author__ = "iVoid1"
# Placeholder, modified by dynamic-versioning.
__version__ = "0.0.0"

__path__ = __import__("pkgutil").extend_path(__path__, __name__)

import logging
from typing import Literal, NamedTuple

class VersionInfo(NamedTuple):
    major: int
    minor: int
    micro: int
    releaselevel: Literal["alpha", "beta", "candidate", "final"]
    serial: int
    metadata: str


# Placeholder, modified by dynamic-versioning.
version_info: VersionInfo = VersionInfo(0, 0, 0, "final", 0, "")

logging.getLogger(__name__).addHandler(logging.NullHandler())