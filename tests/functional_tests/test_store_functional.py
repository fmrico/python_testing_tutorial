"""Functional tests for the base Store class."""

import subprocess


def test_main_script_runs():
    """Comprobar cómo interactúan varios componentes del sistema entre sí.

    Por ejemplo, se podría probar cómo una tienda maneja múltiples tipos de
    muebles con operaciones encadenadas.
    """
    result = subprocess.run(['python3', 'main.py'], capture_output=True,
                            text=True)
    assert 'Initial inventory' in result.stdout
    assert 'Selling item 2' in result.stdout
    assert result.returncode == 0
