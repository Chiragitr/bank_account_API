# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-02 10:34
from __future__ import unicode_literals

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('bank_account', '0008_auto_20180702_0931'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank_account',
            name='created',
            field=django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created'),
        ),
        migrations.AlterField(
            model_name='bank_account',
            name='modified',
            field=django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified'),
        ),
    ]
