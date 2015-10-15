# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipcms', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='role',
            field=models.OneToOneField(default=b'patient', to='ipcms.PermissionsRole'),
        ),
    ]
