import pytest
from fixture.application import Application

@pytest.fixture(scope = "session")
def app(request): #функция создающая фикстуру
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture