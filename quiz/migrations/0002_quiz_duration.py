# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
import timedelta.fields


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='quiz',
            name='duration',
            field=timedelta.fields.TimedeltaField(help_text='Maximum time allowed for the quiz.', verbose_name='Duration', blank=True),
        ),
    ]
