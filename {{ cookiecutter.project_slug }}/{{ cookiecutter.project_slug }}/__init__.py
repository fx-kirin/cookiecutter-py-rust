from ._version import __version__

try:
    from . import rust_binidng
except ImportError:
    pass
