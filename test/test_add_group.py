# -*- coding: utf-8 -*-
from model.group import Group

def test_add_group(app):
    #сохраняем старый список групп. Загружать список будем при помощи вспом. функции , кот. поместим в помощник(grouphelper) по работе с группами app. ....
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="group1", header="group-header", footer="group-footer"))
    #получить новый список групп
    new_groups = app.group.get_group_list()
    #убедимся что новый список на 1 длиннее чем старый
    assert len(old_groups) + 1 == len(new_groups)


def test_add_empty_group(app):
    old_groups = app.group.get_group_list()
    app.group.create(Group(name="", header="", footer=""))
    new_groups = app.group.get_group_list()
    assert len(old_groups) + 1 == len(new_groups)

