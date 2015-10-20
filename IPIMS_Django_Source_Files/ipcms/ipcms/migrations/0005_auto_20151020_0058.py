# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipcms', '0004_auto_20151019_1837'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alert',
            name='alert_patient',
            field=models.OneToOneField(null=True, to='ipcms.Patient'),
        ),
    ]
