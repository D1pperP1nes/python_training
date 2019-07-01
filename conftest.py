import pytest
from fixture.application import Application

fixture = None #глобальная переменная


@pytest.fixture
def app(request): #функция создающая фикстуру
    global fixture #объявляем что будем пользоваться этой переменной
    if fixture is None: #если fixture=None, то функцию инициализируем и сразу выполняем логин
        fixture = Application()
    else:
        if not fixture.is_valid(): #если фикстура не валидна то перезапускаем
            fixture = Application()
    fixture.session.ensure_login(username="admin", password="secret")
    return fixture

@pytest.fixture(scope="session", autouse=True)
def stop(request):
    def fin():
        fixture.session.ensure_logout()
        fixture.destroy()
    request.addfinalizer(fin)
    return fixture