# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipcms', '0024_patientappt_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patientappt',
            name='doctor',
            field=models.ForeignKey(default=b'Select A Doctor..', to='ipcms.Doctor'),
        ),
    ]
