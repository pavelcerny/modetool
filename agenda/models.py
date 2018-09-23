# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


# Create your models here.


class Entry(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class TemplateItem(models.Model):
    label = models.CharField(max_length=200)

    def __str__(self):
        return self.label


class EntryItem(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    template_item = models.ForeignKey(TemplateItem, on_delete=models.CASCADE)
    value = models.CharField(max_length=100000)

    def __str__(self):
        return self.value
