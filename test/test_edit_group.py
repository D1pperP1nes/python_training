from model.group import Group

def test_edit_first_group(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="edited-group1", header="edited-group-header", footer="edited-group-footer"))
    app.session.logout()