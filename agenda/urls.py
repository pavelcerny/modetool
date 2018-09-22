from django.conf.urls import url

from . import views

urlpatterns = [
    # url('', views.index, name='index'),

    # ex /agenda/
    url('', views.agenda, name='agenda'),
    # ex /agenda/5
    url('<int:entry_id>/', views.entry, name='entry'),
    # ex /agenda/template
    url('template/', views.template, name='template'),
]