# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0002_quiz_duration'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='duration',
            field=models.DurationField(help_text='Maximum time allowed for the quiz.', verbose_name='Duration', blank=True),
        ),
    ]
