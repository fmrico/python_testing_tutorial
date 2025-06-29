"""Chair class definition."""

from .furniture import Furniture


class Chair(Furniture):
    """Chair with color attribute."""

    def __init__(self, item_id: int, price: float, color: str):
        """Initialize a chair with nice color."""
        super().__init__(item_id, price)
        self.color = color

    def print_info(self):
        """Print a description of the chair."""
        print(
            f'Chair (ID: {self.item_id}) - Price: {self.price:.2f}'
            f' - Color: {self.color}'
        )
