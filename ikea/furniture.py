"""Base class for all furniture items."""


class Furniture:
    """Generic IKEA furniture."""

    def __init__(self, item_id: int, price: float):
        """Initialize a furniture item with ID and price."""
        self.item_id = item_id
        self.price = price

    def print_info(self):
        """Print a generic description of the furniture."""
        print(f'Furniture (ID: {self.item_id}) - Price: {self.price:.2f}')
