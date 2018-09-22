# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# Register your models here.
from django.contrib import admin

from .models import Entry, EntryItem, TemplateItem

admin.site.register(Entry)
admin.site.register(EntryItem)
admin.site.register(TemplateItem)
