from model.group import Group

def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="group2", header="group-header2", footer="group-footer2"))
    app.group.edit_first_group(Group(name="edited-group"))

def test_edit_group_header(app):
    if app.group.count() == 0:
        app.group.create(Group(name="group2", header="group-header2", footer="group-footer2"))
    app.group.edit_first_group(Group(header="edited-group-header"))

def test_edit_group_footer(app):
    if app.group.count() == 0:
        app.group.create(Group(name="group2", header="group-header2", footer="group-footer2"))
    app.group.edit_first_group(Group(footer="edited-group-footer"))
