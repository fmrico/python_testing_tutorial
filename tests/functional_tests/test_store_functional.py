"""Functional tests for the base Store class."""


def test_main_script_runs(capsys):
    """Comprobar cómo interactúan varios componentes del sistema entre sí.

    Por ejemplo, se podría probar cómo una tienda maneja múltiples tipos de
    muebles con operaciones encadenadas.
    """
    import main

    main.main()

    captured = capsys.readouterr()
    assert 'Initial inventory' in captured.out
    assert 'Selling item 2' in captured.out
