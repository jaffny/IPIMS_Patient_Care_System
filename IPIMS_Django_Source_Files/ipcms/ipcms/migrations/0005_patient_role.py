# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipcms', '0004_auto_20151009_2024'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='role',
            field=models.OneToOneField(default=b'', blank=True, to='ipcms.PermissionsRoles'),
        ),
    ]
