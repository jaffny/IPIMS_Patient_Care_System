# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ipcms', '0003_auto_20151011_0252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temppatientdata',
            name='user',
            field=models.ForeignKey(to='ipcms.Patient', default='Select a patient', null=True, unique=True),
        ),
    ]
