"""Tests for the Chair class."""

from ikea.chair import Chair


def test_chair_attributes():
    """Test Chair attribute assignment."""
    chair = Chair(item_id=1, price=59.99, color='Blue')
    assert chair.item_id == 1
    assert chair.price == 59.99
    assert chair.color == 'Blue'


def test_chair_print_info(capsys):
    """Test Chair.print() output."""
    chair = Chair(item_id=1, price=59.99, color='Blue')
    chair.print_info()
    captured = capsys.readouterr()
    assert 'Chair' in captured.out
    assert 'Blue' in captured.out
