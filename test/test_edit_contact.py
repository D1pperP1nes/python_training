from model.contact import Contact


def test_edit_contact_firstname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(firstname="Dmitry"))
    app.contact.edit_first_contact(Contact(firstname="Ivan"))

def test_edit_contact_middlename(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(middlename="Y"))
    app.contact.edit_first_contact(Contact(middlename="Ivanovich"))

def test_edit_contact_lastname(app):
    if app.contact.count() == 0:
        app.contact.create(Contact(lastname="Gdjfhks"))
    app.contact.edit_first_contact(Contact(lastname="Ivanov"))
