# 🪑 IKEA Inventory Simulator

This project is a Python package named `ikea` that simulates a basic inventory system for an IKEA-like furniture store. It is designed to serve as a practical tutorial for Python packaging and testing.

## 🚀 Functionality

The `ikea` package provides:

- A base `Furniture` class with `id` and `price`.
- Specialized furniture items:
  - `Chair` (with `color`)
  - `Table` (with number of `seats`)
  - `Lamp` (with number of `bulbs` and `bulb_type`)
  - `Plant` (with `plant_type` and indoor/outdoor flag)
- A `Store` class to:
  - Add, remove, and get furniture
  - Sell items
  - List inventory

Example usage is provided in `main.py`.

## 📦 Project Structure

```
ikea_project/
├── ikea/                 # Main package
│   ├── furniture.py      # Base class
│   ├── chair.py          # Chair class
│   ├── table.py          # Table class
│   ├── lamp.py           # Lamp class
│   ├── plant.py          # Plant class
│   ├── store.py          # Store class
│   └── __init__.py
├── main.py               # Example script
├── unit_tests/           # Unit tests
├── integration_tests/    # Integration tests
├── functional_tests/     # Functional tests
├── setup.py
├── requirements.txt      # (Optional) dependencies
├── pytest.ini
└── .github/workflows/    # GitHub Actions
```

## 🛠 Installation (editable mode)

To install the package locally in editable mode:

```bash
pip install -e .
```

This allows you to import `ikea` while working on the source code directly.

## ▶️ How to Run

You can run the example script with:

```bash
python main.py
```

It creates a store, adds furniture items, and performs basic operations (list, sell, etc.).

## ✅ How to Run Tests

Make sure you have `pytest` and `pytest-cov` installed:

```bash
pip install pytest pytest-cov
```

### Run all tests:

```bash
pytest
```

### Run with coverage:

```bash
pytest --cov=ikea --cov-report=term
```

### Optional: enforce minimum coverage

```bash
coverage report --fail-under=90
```

## 🧪 Test Types

This project includes:

- Unit tests (`unit_tests/`)
- Integration tests (`integration_tests/`)
- Functional tests (`functional_tests/`)

Use the `pytest.ini` to configure which folders to test.

## 🤖 Continuous Integration

This repository includes GitHub Actions to run tests and check code coverage automatically on push and pull requests to `main`.

---

## 📚 License

MIT License (or update if needed)
