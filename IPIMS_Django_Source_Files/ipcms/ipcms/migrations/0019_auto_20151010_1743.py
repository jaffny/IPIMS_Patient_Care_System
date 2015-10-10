# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipcms', '0018_auto_20151010_0757'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='user',
        ),
        migrations.AddField(
            model_name='patient',
            name='user_role',
            field=models.OneToOneField(default=b'', to='ipcms.PermissionsRole'),
        ),
    ]
