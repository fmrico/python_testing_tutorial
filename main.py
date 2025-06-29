"""Example script to use the ikea package."""

from ikea import Chair, Lamp, Plant, Store, Table


def main():
    """Create a store, add items, and demonstrate functionality."""
    store = Store()

    store.add(Chair(item_id=1, price=49.99, color='Red'))
    store.add(Table(item_id=2, price=149.99, seats=6))
    store.add(Lamp(item_id=3, price=19.99, bulbs=2, bulb_type='LED'))
    store.add(Plant(item_id=4, price=9.99, plant_type='Ficus', indoor=True))

    print('\nInitial inventory:')
    store.list_inventory()

    print('\nSelling item 2:')
    store.sell(2)

    print('\nInventory after selling:')
    store.list_inventory()


if __name__ == '__main__':
    main()
