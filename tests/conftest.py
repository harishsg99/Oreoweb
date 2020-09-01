import pytest

import oreoweb


@pytest.fixture
def app():
    return oreoweb.oreoweb(templates_dir="tests/templates", debug=False)


@pytest.fixture
def client(app):
    return app.session()
