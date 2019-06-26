from model.group import Group

def test_edit_group_name(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(name="edited-group"))
    app.session.logout()

def test_edit_group_header(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(header="edited-group-header"))
    app.session.logout()

def test_edit_group_footer(app):
    app.session.login(username="admin", password="secret")
    app.group.edit_first_group(Group(footer="edited-group-footer"))
    app.session.logout()