"""Integration tests for the base Store class."""

from ikea.chair import Chair
from ikea.lamp import Lamp
from ikea.store import Store
from ikea.table import Table


def test_store_inventory_flow():
    """Comprobar cómo interactúan varios componentes del sistema entre sí.

    Por ejemplo, se podría probar cómo una tienda maneja múltiples tipos de
    muebles con operaciones encadenadas.
    """
    store = Store()
    store.add(Chair(1, 50.0, 'Blue'))
    store.add(Table(2, 200.0, 6))
    store.add(Lamp(3, 30.0, 2, 'LED'))

    assert store.get(1).color == 'Blue'
    assert store.sell(2).seats == 6
    assert store.get(2) is None
