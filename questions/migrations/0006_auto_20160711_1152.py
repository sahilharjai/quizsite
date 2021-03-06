# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-07-11 06:22
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('questions', '0005_auto_20160624_1117'),
    ]

    operations = [
        migrations.AlterField(
            model_name='test',
            name='quiz',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_quiz', to='questions.Quiz'),
        ),
        migrations.AlterField(
            model_name='test',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='test_user', to=settings.AUTH_USER_MODEL),
        ),
    ]
