# -*- coding: utf-8 -*-
# Generated by Django 1.9.2 on 2016-06-15 15:18
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('questions', '0002_choice'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Answer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='ans_selected', to='questions.Choice')),
                ('answer_to', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_given', to='questions.Question')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='answer_created', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
