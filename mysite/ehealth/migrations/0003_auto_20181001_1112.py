# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-10-01 11:12
from __future__ import unicode_literals
from django.utils import timezone
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ehealth', '0002_auto_20181001_1111'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='dob',
            field=models.DateField(default=timezone.now, verbose_name='date of birth'),
        ),
    ]
