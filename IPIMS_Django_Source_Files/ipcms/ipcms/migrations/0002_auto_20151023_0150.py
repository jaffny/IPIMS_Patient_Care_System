# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipcms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientappt',
            name='doctor',
            field=models.ForeignKey(default=-1, to='ipcms.Doctor'),
        ),
    ]
