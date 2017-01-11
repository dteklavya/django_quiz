# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TF_Question',
            fields=[
                ('question_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='quiz.Question')),
                ('correct', models.BooleanField(default=False, help_text='Tick this if the question is true. Leave it blank for false.', verbose_name='Correct')),
            ],
            options={
                'ordering': ['category'],
                'verbose_name': 'True/False Question',
                'verbose_name_plural': 'True/False Questions',
            },
            bases=('quiz.question',),
        ),
    ]
