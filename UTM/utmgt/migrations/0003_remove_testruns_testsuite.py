# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utmgt', '0002_auto_20160525_1307'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='testruns',
            name='testSuite',
        ),
    ]
