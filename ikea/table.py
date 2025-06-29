"""Table class definition."""

from .furniture import Furniture


class Table(Furniture):
    """Table with number of seats."""

    def __init__(self, item_id: int, price: float, seats: int):
        """Initialize a table with seat count."""
        super().__init__(item_id, price)
        self.seats = seats

    def print_info(self):
        """Print a description of the table."""
        print(
            f'Table (ID: {self.item_id}) - Price: {self.price:.2f} - '
            f'Seats: {self.seats}'
        )
