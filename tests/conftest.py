import pytest
from todoApp import application

@pytest.fixture(scope='module')
def app():
    return application