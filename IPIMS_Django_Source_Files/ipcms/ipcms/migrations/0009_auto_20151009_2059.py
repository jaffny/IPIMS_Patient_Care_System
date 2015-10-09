# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipcms', '0008_remove_patient_role'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='PermissionsRoles',
            new_name='PermissionsRole',
        ),
    ]
