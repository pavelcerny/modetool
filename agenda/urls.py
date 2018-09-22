from django.conf.urls import url

from . import views

urlpatterns = [
    # ex /agenda/
    url('^$', views.agenda, name='show_agenda'),
    # ex /agenda/5
    url('^<int:entry_id>$', views.entry, name='show_entry'),
    # ex /agenda/template
    url('^template$', views.template, name='show_template'),
]