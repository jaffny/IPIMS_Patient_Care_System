# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipcms', '0002_auto_20151014_0614'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='role',
        ),
    ]
