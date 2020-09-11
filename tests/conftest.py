import pytest

import oreoweb


@pytest.fixture
def app():
    return oreoweb.Oreoweb(templates_dir="tests/templates", debug=False)


@pytest.fixture
def client(app):
    return app.session()
