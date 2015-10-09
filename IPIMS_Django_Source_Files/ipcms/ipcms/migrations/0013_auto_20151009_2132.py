# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipcms', '0012_doctor'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='doctor',
            name='doctor_name',
        ),
        migrations.AddField(
            model_name='doctor',
            name='doctor_first_name',
            field=models.CharField(default=b'', max_length=256),
        ),
        migrations.AddField(
            model_name='doctor',
            name='doctor_last_name',
            field=models.CharField(default=b'', max_length=256),
        ),
        migrations.AddField(
            model_name='doctor',
            name='doctor_type',
            field=models.CharField(default=b'Select Doctor Type', max_length=256, choices=[(b'Gynecologist', b'Gynecologist'), (b'Neuro', b'Neuro')]),
        ),
    ]
