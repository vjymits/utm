# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utmgt', '0005_auto_20160525_1519'),
    ]

    operations = [
        migrations.AddField(
            model_name='testsuites',
            name='report',
            field=models.URLField(max_length=256, null=True, blank=True),
        ),
        migrations.AddField(
            model_name='testsuites',
            name='reviewUri',
            field=models.URLField(max_length=256, null=True, blank=True),
        ),
    ]
