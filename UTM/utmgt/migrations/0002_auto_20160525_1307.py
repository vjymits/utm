# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('utmgt', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='testruns',
            old_name='description1',
            new_name='description',
        ),
    ]
