# -*- coding: utf-8 -*-
import pytest
from model.contact import Contact
from fixture.application import Application


@pytest.fixture
def app(request):
    fixture = Application()
    request.addfinalizer(fixture.destroy)
    return fixture


def test_add_contact(app):
    app.login(username="admin", password="secret")
    app.create_contact(Contact(firstname="Dmitry", middlename="Y", lastname="Gdjfhks", nickname="jjjjjjjj",
                            title="kkkkkkkkkkk", company="lllllllllllll", address="shfhkhkdsh", home="lksjdfkljhsf",
                            mobile="+78342235252", work="38764823764826", fax="342425", email="fgdgd@kjhg.com",
                            homepage="localhost/addressbook/", birth_year="1908", address2="fgdgfgd", phone2="dghdhd",
                            bday="1", bmonth="January"))
    app.logout()
