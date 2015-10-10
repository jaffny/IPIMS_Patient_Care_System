# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipcms', '0020_auto_20151010_1743'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='user_role',
            field=models.ForeignKey(default=b'', to='ipcms.PermissionsRole', null=True),
        ),
    ]
