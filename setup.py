"""Setup script for the ikea package.

This file is used to define how the package should be installed.
It tells Python tools like pip:
- the name of the package,
- its version,
- where to find the code,
- and any other metadata needed for installation.

To install this package in editable (development) mode, run:
    pip install -e .

This allows you to import 'ikea' from your code without moving files
or copying anything, and changes to the code will be reflected immediately.
"""

from setuptools import find_packages, setup

setup(
    name='ikea',
    version='0.1',
    packages=find_packages(),
    python_requires='>=3.6',
)
