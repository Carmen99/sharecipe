# -*- coding: utf-8 -*-
# Generated by Django 1.11.8 on 2017-12-17 14:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('list', '0003_auto_20171217_1510'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='images/None/no-img.jpg', upload_to='../images/'),
        ),
    ]
