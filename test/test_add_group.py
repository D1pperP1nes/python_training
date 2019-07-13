# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    #сохраняем старый список групп. Загружать список будем при помощи вспом. функции , кот. поместим в помощник(grouphelper) по работе с группами app. ....
    old_groups = app.group.get_group_list()
    group = Group(name="group1", header="group-header", footer="group-footer")
    app.group.create(group)
    #получить новый список групп
    new_groups = app.group.get_group_list()
    #убедимся что новый список на 1 длиннее чем старый
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    group = Group(name="", header="", footer="")
    app.group.create(group)
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)
    old_groups.append(group)
    assert sorted(old_groups, key=Group.id_or_max) == sorted(new_groups, key=Group.id_or_max)


