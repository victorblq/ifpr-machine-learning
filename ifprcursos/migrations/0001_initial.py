# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-25 18:04
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Alternativa',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('descricao', models.CharField(default='erro', max_length=150)),
                ('valor', models.IntegerField(verbose_name='valor')),
            ],
        ),
        migrations.CreateModel(
            name='Pergunta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Resposta',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('q1', models.IntegerField(verbose_name='q1')),
                ('q2', models.IntegerField(verbose_name='q2')),
                ('q3', models.IntegerField(verbose_name='q3')),
                ('q4', models.IntegerField(verbose_name='q4')),
                ('q5', models.IntegerField(verbose_name='q5')),
                ('q6', models.IntegerField(verbose_name='q6')),
                ('q7', models.IntegerField(verbose_name='q7')),
                ('q8', models.IntegerField(verbose_name='q8')),
                ('q9', models.IntegerField(verbose_name='q9')),
                ('q10', models.IntegerField(verbose_name='q10')),
                ('q11', models.IntegerField(verbose_name='q11')),
                ('q12', models.IntegerField(verbose_name='q12')),
                ('curso', models.IntegerField(verbose_name='curso')),
            ],
        ),
        migrations.AddField(
            model_name='alternativa',
            name='pergunta',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ifprcursos.Pergunta'),
        ),
    ]
