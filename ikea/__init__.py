"""Top-level package for ikea furniture inventory."""

from .chair import Chair
from .furniture import Furniture
from .lamp import Lamp
from .plant import Plant
from .store import Store
from .table import Table

__all__ = ['Furniture', 'Chair', 'Table', 'Lamp', 'Plant', 'Store']
