# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipcms', '0022_auto_20151010_1746'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patientappt',
            name='date',
        ),
    ]
