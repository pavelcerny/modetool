from django.conf.urls import url

from . import views

urlpatterns = [
    # ex /agenda/
    url(r'^$', views.agenda, name='show_agenda'),
    # ex /agenda/5
    url(r'^(?P<entry_id>[0-9]+)$', views.entry, name='show_entry'),
    url(r'^(?P<entry_id>[0-9]+)/delete$', views.delete_entry, name='delete_entry'),
    # ex /agenda/template
    url(r'^template$', views.template, name='show_template'),
    url(r'^template_item/(?P<template_item_id>[0-9]+)/delete$', views.delete_template_item,
        name='delete_template_item'),
    # ex /agenda/todolist
    url('^todolist$', views.todolist, name='show_todo'),

    # API
    url(r'^api/entry$', views.EntryList.as_view()),
    url(r'^api/entry/(?P<pk>[0-9]+)$', views.EntryDetail.as_view()),
]