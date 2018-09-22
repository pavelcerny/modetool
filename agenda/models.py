# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class Entry(models.Model):
    name = models.CharField(max_length=200)


class EntryItem(models.Model):
    entry = models.ForeignKey(Entry, on_delete=models.CASCADE)
    label = models.CharField(max_length=200)
    value = models.CharField(max_length=100000)


class TemplateItem(models.Model):
    label = models.CharField(max_length=200)