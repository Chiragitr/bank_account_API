# -*- coding: utf-8 -*-
# Generated by Django 1.11.13 on 2018-07-02 08:13
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank_account', '0003_customer_bank_detail_branch_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='bank_details',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_holder_name', models.CharField(max_length=200)),
                ('account_no', models.IntegerField()),
                ('ifsc_code', models.IntegerField()),
                ('branch_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Customer_bank_detail',
        ),
    ]
