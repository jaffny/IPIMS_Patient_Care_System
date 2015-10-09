# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipcms', '0006_auto_20151009_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='role',
            field=models.OneToOneField(default=b'test', to='ipcms.PermissionsRoles'),
        ),
    ]
