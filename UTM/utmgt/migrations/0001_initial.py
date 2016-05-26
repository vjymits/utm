# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='TestCases',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('description', models.CharField(max_length=256, null=True, blank=True)),
                ('created', models.BigIntegerField(null=True, blank=True)),
                ('submitter', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'db_table': 'utm_test_cases',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TestRuns',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('result', models.CharField(default=b'untested', max_length=10, choices=[(b'untested', b'Untested'), (b'passed', b'Passed'), (b'failed', b'Failed'), (b'retest', b'Retest'), (b'blocked', b'Blocked')])),
                ('description1', models.CharField(max_length=256, null=True, blank=True)),
                ('attach', models.FilePathField(null=True, blank=True)),
                ('created', models.BigIntegerField(null=True, blank=True)),
                ('submitter', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
                ('testCase', models.ForeignKey(blank=True, to='utmgt.TestCases', null=True)),
            ],
            options={
                'db_table': 'utm_test_reports',
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='TestSuites',
            fields=[
                ('id', models.AutoField(serialize=False, primary_key=True)),
                ('name', models.CharField(max_length=100, null=True, blank=True)),
                ('description', models.CharField(max_length=256, null=True, blank=True)),
                ('created', models.BigIntegerField(null=True, blank=True)),
                ('submitter', models.ForeignKey(blank=True, to=settings.AUTH_USER_MODEL, null=True)),
            ],
            options={
                'db_table': 'utm_test_suites',
                'managed': True,
            },
        ),
        migrations.AddField(
            model_name='testruns',
            name='testSuite',
            field=models.ForeignKey(blank=True, to='utmgt.TestSuites', null=True),
        ),
        migrations.AddField(
            model_name='testcases',
            name='testSuite',
            field=models.ForeignKey(blank=True, to='utmgt.TestSuites', null=True),
        ),
    ]
