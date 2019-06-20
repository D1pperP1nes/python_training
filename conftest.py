import pytest
from fixture.application import Application

@pytest.fixture
def app(request): #функция создающая фикстуру
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture