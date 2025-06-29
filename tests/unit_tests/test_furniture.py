"""Tests for the base Furniture class."""

from ikea.furniture import Furniture


def test_furniture_init():
    """Test Furniture initialization."""
    item = Furniture(item_id=100, price=123.45)
    assert item.item_id == 100
    assert item.price == 123.45
