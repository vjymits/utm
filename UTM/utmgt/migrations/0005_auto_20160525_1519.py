# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utmgt', '0004_testcases_result'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testcases',
            old_name='description',
            new_name='testCase',
        ),
        migrations.AddField(
            model_name='testcases',
            name='output',
            field=models.FileField(null=True, upload_to=b'', blank=True),
        ),
    ]
