from model.contact import Contact


def test_edit_contact_firstname(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(firstname="Ivan"))
    app.session.logout()

def test_edit_contact_middlename(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(middlename="Ivanovich"))
    app.session.logout()

def test_edit_contact_lastname(app):
    app.session.login(username="admin", password="secret")
    app.contact.edit_first_contact(Contact(lastname="Ivanov"))
    app.session.logout()