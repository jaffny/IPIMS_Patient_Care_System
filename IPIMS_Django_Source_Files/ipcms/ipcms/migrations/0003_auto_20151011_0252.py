# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ipcms', '0002_auto_20151011_0240'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temppatientdata',
            name='user',
            field=models.ForeignKey(to='ipcms.Patient', unique=True, null=True),
        ),
    ]
