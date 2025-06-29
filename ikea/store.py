"""Store class for managing inventory."""


class Store:
    """IKEA Store inventory system."""

    def __init__(self):
        """Initialize an empty store inventory."""
        self.inventory = {}

    def add(self, furniture):
        """Add a furniture item to the store."""
        self.inventory[furniture.item_id] = furniture

    def remove(self, item_id: int):
        """Remove a furniture item from the store by ID."""
        return self.inventory.pop(item_id, None)

    def get(self, item_id: int):
        """Retrieve a furniture item by ID."""
        return self.inventory.get(item_id)

    def sell(self, item_id: int):
        """Sell (remove and report) a furniture item by ID."""
        item = self.remove(item_id)
        if item:
            print(f'Selling item {item_id} for {item.price:.2f}')
            return item
        print(f'Item {item_id} not found.')
        return None

    def list_inventory(self):
        """Print the full inventory."""
        for item in self.inventory.values():
            item.print_info()
