# -*- coding: utf-8 -*-
from model.contact import Contact


def test_add_contact(app):
    app.contact.create(Contact(firstname="Dmitry", middlename="Y", lastname="Gdjfhks", nickname="jjjjjjjj",
                               title="kkkkkkkkkkk", company="lllllllllllll", address="shfhkhkdsh", home="lksjdfkljhsf",
                               mobile="+78342235252", work="38764823764826", fax="342425", email="fgdgd@kjhg.com",
                               homepage="localhost/addressbook/", birth_year="1908", address2="fgdgfgd", phone2="dghdhd",
                               bday="1", bmonth="January"))
