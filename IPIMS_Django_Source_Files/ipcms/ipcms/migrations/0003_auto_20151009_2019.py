# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipcms', '0002_auto_20151009_2016'),
    ]

    operations = [
        migrations.CreateModel(
            name='PermissionsRoles',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role', models.CharField(max_length=256, choices=[(b'admin', b'admin'), (b'nurse', b'nurse'), (b'staff', b'staff'), (b'doctor', b'doctor'), (b'patient', b'patient'), (b'lab', b'lab')])),
            ],
        ),
        migrations.RemoveField(
            model_name='patient',
            name='role',
        ),
    ]
