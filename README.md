# Python-build-framework

This is a standard build framework setting some basics to easily get going building new python packages. For using this framework for your own packages, either create a new repository with this as a basis or fork the current repos.

## Poetry

The framework is based on Poetry dependence manager, and the only thing to do to initiate the current framework is:

'''bash
poetry install
'''

The packages for running the the program and framework will then be installed. For adding more packages and features to the current setup, please refer to the (https://python-poetry.org/docs/)[Poetry documentation].

After installing the initial sample package can be run by
'''bash
poetry run python3 main.py
'''

## Pytest

A standard setup for pytest has also been installed. Tests are located in the test-catalog. In order to add more tests to written code, just add new files with tests in the test catalog. Tests for module_name.py should be named test_module_name.py. To run existing tests, just run

'''bash
poetry run pytest
'''

For more information on how to configure pytest, refer to the (https://docs.pytest.org/en/7.1.x/contents.html)[Pytest documentation]

## Pre-commit checks

There are a number of linting and standard packages configure for running on every commit in Github. These are configured in the
'''
.pre-commit-config.yaml
'''
file. These pre-commit hooks are run on every commit in Github through through the Github workflow file
'''
.github/workflows/main.yaml
'''

These pre-commit hooks can be run locally by running
'''bash
poetry run pre-commit run --all-files
'''
in a terminal
