# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utmgt', '0007_auto_20160526_1433'),
    ]

    operations = [
        migrations.AlterField(
            model_name='testsuites',
            name='report',
            field=models.FileField(max_length=256, null=True, upload_to=b'', blank=True),
        ),
    ]
