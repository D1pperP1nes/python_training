from model.contact import Contact


def test_edit_contact_firstname(app):
    app.contact.edit_first_contact(Contact(firstname="Ivan"))

def test_edit_contact_middlename(app):
    app.contact.edit_first_contact(Contact(middlename="Ivanovich"))

def test_edit_contact_lastname(app):
    app.contact.edit_first_contact(Contact(lastname="Ivanov"))
