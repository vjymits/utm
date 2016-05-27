# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utmgt', '0006_auto_20160525_1628'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testsuites',
            name='report',
            field=models.FilePathField(max_length=256, null=True, blank=True),
        ),
    ]
