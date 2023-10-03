"""App package."""

import importlib.metadata

if not __name__.startswith("src"):
    # Set version from metadata if package is not being run from source.
    __version__: str = importlib.metadata.version(__package__ or __name__)
