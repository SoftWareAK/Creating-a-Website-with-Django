# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2021-09-24 08:23
from __future__ import unicode_literals

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0002_auto_20210923_1645'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=ckeditor.fields.RichTextField(verbose_name='içerik'),
        ),
    ]
