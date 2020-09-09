# -*- coding: utf-8 -*-
# Generated by Django 1.11.20 on 2019-05-23 02:12
from __future__ import unicode_literals

from decimal import Decimal
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PurchaseRequisition',
            fields=[
                ('pr_id', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('description', models.TextField(blank=True, default=None, null=True)),
                ('time_created', models.DateTimeField()),
                ('total_price', models.DecimalField(decimal_places=2, default=Decimal('0.00'), max_digits=10)),
                ('status', models.TextField(default='Pending', max_length=10)),
                ('person_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Person')),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseRequisitionItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('unit_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('total_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('quantity', models.IntegerField()),
                ('ref_id', models.CharField(blank=True, default=None, max_length=20, null=True)),
                ('item_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Item')),
                ('pr_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='PurchaseRequisition.PurchaseRequisition')),
            ],
        ),
        migrations.AlterUniqueTogether(
            name='purchaserequisitionitem',
            unique_together=set([('pr_id', 'item_id')]),
        ),
    ]
