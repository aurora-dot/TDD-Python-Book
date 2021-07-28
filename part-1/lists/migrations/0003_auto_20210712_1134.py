# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-07-12 11:34
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("lists", "0002_item_text"),
    ]

    operations = [
        migrations.CreateModel(
            name="List",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="item",
            name="list",
            field=models.ForeignKey(
                default=None,
                on_delete=django.db.models.deletion.CASCADE,
                to="lists.List",
            ),
        ),
    ]
