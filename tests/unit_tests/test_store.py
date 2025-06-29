"""Tests for the Store class."""

from ikea.store import Store
from ikea.table import Table


def test_add_and_get_item():
    """Test adding and retrieving items from the store."""
    store = Store()
    table = Table(item_id=42, price=199.99, seats=4)
    store.add(table)
    retrieved = store.get(42)
    assert retrieved is table


def test_remove_item():
    """Test removing an item from the store."""
    store = Store()
    table = Table(item_id=1, price=100.0, seats=4)
    store.add(table)
    removed = store.remove(1)
    assert removed is table
    assert store.get(1) is None


def test_sell_item(capsys):
    """Test selling an item from the store."""
    store = Store()
    table = Table(item_id=5, price=200.0, seats=6)
    store.add(table)
    sold = store.sell(5)
    assert sold.item_id == 5
    captured = capsys.readouterr()
    assert 'Selling item 5' in captured.out
