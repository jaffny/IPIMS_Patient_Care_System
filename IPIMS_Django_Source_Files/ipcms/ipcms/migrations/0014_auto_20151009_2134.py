# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipcms', '0013_auto_20151009_2132'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientappt',
            name='doctor',
            field=models.ForeignKey(default=b'', blank=True, to='ipcms.Doctor'),
        ),
    ]
