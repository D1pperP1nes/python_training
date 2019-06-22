from model.contact import Contact


def test_add_contact(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="Ivan", middlename="Ivanovich", lastname="Ivanov", nickname="John",
                               title="sometitle", company="microsoft", address="Gorky Street", home="4627799",
                               mobile="+78342235252", work="38764823764826", fax="342425", email="John@microsoft.com",
                               homepage="localhost/addressbook/", birth_year="1998", address2="Tolstoy Street", phone2="4665545",
                               bday="2", bmonth="February"))
    app.session.logout()