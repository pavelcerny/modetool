# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2018-09-23 08:00
from __future__ import unicode_literals

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('agenda', '0003_auto_20180922_1822'),
    ]

    operations = [
        migrations.AddField(
            model_name='entryitem',
            name='template_item',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='agenda.TemplateItem'),
            preserve_default=False,
        ),
    ]