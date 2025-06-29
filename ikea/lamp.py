"""Lamp class definition."""

from .furniture import Furniture


class Lamp(Furniture):
    """Lamp with bulb count and type."""

    def __init__(self, item_id: int, price: float, bulbs: int, bulb_type: str):
        """Initialize a lamp with bulb count and type."""
        super().__init__(item_id, price)
        self.bulbs = bulbs
        self.bulb_type = bulb_type

    def print_info(self):
        """Print a description of the lamp."""
        print(
            f'Lamp (ID: {self.item_id}) - Price: {self.price:.2f} - '
            f'Bulbs: {self.bulbs} ({self.bulb_type})'
        )
