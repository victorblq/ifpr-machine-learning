# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 22:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ifprcursos', '0003_auto_20171125_2125'),
    ]

    operations = [
        migrations.CreateModel(
            name='Curso',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nome', models.CharField(default='erro', max_length=150)),
                ('valor', models.IntegerField(verbose_name='valor')),
            ],
        ),
    ]