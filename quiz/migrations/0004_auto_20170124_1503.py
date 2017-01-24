# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('quiz', '0003_auto_20170112_0759'),
    ]

    operations = [
        migrations.AlterField(
            model_name='quiz',
            name='duration',
            field=models.DurationField(help_text='Maximum time allowed for the quiz.', null=True, verbose_name='Duration', blank=True),
        ),
    ]
