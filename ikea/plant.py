"""Plant class definition."""

from .furniture import Furniture


class Plant(Furniture):
    """Plant with type and indoor/outdoor info."""

    def __init__(self, item_id: int, price: float, plant_type: str,
                 indoor: bool):
        """Initialize a plant with type and location."""
        super().__init__(item_id, price)
        self.plant_type = plant_type
        self.indoor = indoor

    def print_info(self):
        """Print a description of the plant."""
        location = 'Indoor' if self.indoor else 'Outdoor'
        print(
            f'Plant (ID: {self.item_id}) - Price: {self.price:.2f} - '
            f'Type: {self.plant_type} - {location}'
        )
