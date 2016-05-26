# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utmgt', '0003_remove_testruns_testsuite'),
    ]

    operations = [
        migrations.AddField(
            model_name='testcases',
            name='result',
            field=models.CharField(default=b'untested', max_length=10, choices=[(b'untested', b'Untested'), (b'passed', b'Passed'), (b'failed', b'Failed'), (b'retest', b'Retest'), (b'blocked', b'Blocked')]),
        ),
    ]
