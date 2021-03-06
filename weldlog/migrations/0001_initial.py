# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-08-23 15:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Weld',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=150)),
                ('pipe_size', models.IntegerField()),
                ('pipe_thickness', models.IntegerField()),
                ('type',
                 models.CharField(choices=[('FW', 'Field Weld'), ('SW', 'Shop Weld')], default='FW', max_length=2)),
                ('disposition',
                 models.CharField(choices=[('NA', ''), ('ACC', 'Accepted'), ('REJ', 'Rejected')], default='NA',
                                  max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Welder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('stencil', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='weld',
            name='welders',
            field=models.ManyToManyField(to='weldlog.Welder'),
        ),
    ]
