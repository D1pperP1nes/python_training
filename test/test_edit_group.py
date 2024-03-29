from model.group import Group

def test_edit_group_name(app):
    if app.group.count() == 0:
        app.group.create(Group(name="group2", header="group-header2", footer="group-footer2"))
    old_groups = app.group.get_group_list()
    group = Group(name="edited-group")
    group.id = old_groups[0].id #запоминаем старый идентификатор
    app.group.edit_first_group(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) == len(new_groups)
    old_groups[0] = group
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)



#def test_edit_group_header(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="group2", header="group-header2", footer="group-footer2"))
#    old_groups = app.group.get_group_list()
#    app.group.edit_first_group(Group(header="edited-group-header"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)


#def test_edit_group_footer(app):
#    if app.group.count() == 0:
#        app.group.create(Group(name="group2", header="group-header2", footer="group-footer2"))
#    old_groups = app.group.get_group_list()
#    app.group.edit_first_group(Group(footer="edited-group-footer"))
#    new_groups = app.group.get_group_list()
#    assert len(old_groups) == len(new_groups)

