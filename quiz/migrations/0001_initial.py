# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('category', models.CharField(max_length=250, unique=True, null=True, verbose_name='Category', blank=True)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categories',
            },
        ),
        migrations.CreateModel(
            name='Progress',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('score', models.CommaSeparatedIntegerField(max_length=1024, verbose_name='Score')),
                ('user', models.OneToOneField(verbose_name='User', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User Progress',
                'verbose_name_plural': 'User progress records',
            },
        ),
        migrations.CreateModel(
            name='Question',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('figure', models.ImageField(upload_to='uploads/%Y/%m/%d', null=True, verbose_name='Figure', blank=True)),
                ('content', models.CharField(help_text='Enter the question text that you want displayed', max_length=1000, verbose_name='Question')),
                ('explanation', models.TextField(help_text='Explanation to be shown after the question has been answered.', max_length=2000, verbose_name='Explanation', blank=True)),
                ('category', models.ForeignKey(verbose_name='Category', blank=True, to='quiz.Category', null=True)),
            ],
            options={
                'ordering': ['category'],
                'verbose_name': 'Question',
                'verbose_name_plural': 'Questions',
            },
        ),
        migrations.CreateModel(
            name='Quiz',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=60, verbose_name='Title')),
                ('description', models.TextField(help_text='a description of the quiz', verbose_name='Description', blank=True)),
                ('url', models.SlugField(help_text='a user friendly url', max_length=60, verbose_name='user friendly url')),
                ('random_order', models.BooleanField(default=False, help_text='Display the questions in a random order or as they are set?', verbose_name='Random Order')),
                ('max_questions', models.PositiveIntegerField(help_text='Number of questions to be answered on each attempt.', null=True, verbose_name='Max Questions', blank=True)),
                ('answers_at_end', models.BooleanField(default=False, help_text='Correct answer is NOT shown after question. Answers displayed at the end.', verbose_name='Answers at end')),
                ('exam_paper', models.BooleanField(default=False, help_text='If yes, the result of each attempt by a user will be stored. Necessary for marking.', verbose_name='Exam Paper')),
                ('single_attempt', models.BooleanField(default=False, help_text='If yes, only one attempt by a user will be permitted. Non users cannot sit this exam.', verbose_name='Single Attempt')),
                ('pass_mark', models.SmallIntegerField(default=0, help_text='Percentage required to pass exam.', blank=True, verbose_name='Pass Mark', validators=[django.core.validators.MaxValueValidator(100)])),
                ('success_text', models.TextField(help_text='Displayed if user passes.', verbose_name='Success Text', blank=True)),
                ('fail_text', models.TextField(help_text='Displayed if user fails.', verbose_name='Fail Text', blank=True)),
                ('draft', models.BooleanField(default=False, help_text='If yes, the quiz is not displayed in the quiz list and can only be taken by users who can edit quizzes.', verbose_name='Draft')),
                ('category', models.ForeignKey(verbose_name='Category', blank=True, to='quiz.Category', null=True)),
            ],
            options={
                'verbose_name': 'Quiz',
                'verbose_name_plural': 'Quizzes',
            },
        ),
        migrations.CreateModel(
            name='Sitting',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('question_order', models.CommaSeparatedIntegerField(max_length=1024, verbose_name='Question Order')),
                ('question_list', models.CommaSeparatedIntegerField(max_length=1024, verbose_name='Question List')),
                ('incorrect_questions', models.CommaSeparatedIntegerField(max_length=1024, verbose_name='Incorrect questions', blank=True)),
                ('current_score', models.IntegerField(verbose_name='Current Score')),
                ('complete', models.BooleanField(default=False, verbose_name='Complete')),
                ('user_answers', models.TextField(default='{}', verbose_name='User Answers', blank=True)),
                ('start', models.DateTimeField(auto_now_add=True, verbose_name='Start')),
                ('end', models.DateTimeField(null=True, verbose_name='End', blank=True)),
                ('quiz', models.ForeignKey(verbose_name='Quiz', to='quiz.Quiz')),
                ('user', models.ForeignKey(verbose_name='User', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'permissions': (('view_sittings', 'Can see completed exams.'),),
            },
        ),
        migrations.CreateModel(
            name='SubCategory',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('sub_category', models.CharField(max_length=250, null=True, verbose_name='Sub-Category', blank=True)),
                ('category', models.ForeignKey(verbose_name='Category', blank=True, to='quiz.Category', null=True)),
            ],
            options={
                'verbose_name': 'Sub-Category',
                'verbose_name_plural': 'Sub-Categories',
            },
        ),
        migrations.AddField(
            model_name='question',
            name='quiz',
            field=models.ManyToManyField(to='quiz.Quiz', verbose_name='Quiz', blank=True),
        ),
        migrations.AddField(
            model_name='question',
            name='sub_category',
            field=models.ForeignKey(verbose_name='Sub-Category', blank=True, to='quiz.SubCategory', null=True),
        ),
    ]
