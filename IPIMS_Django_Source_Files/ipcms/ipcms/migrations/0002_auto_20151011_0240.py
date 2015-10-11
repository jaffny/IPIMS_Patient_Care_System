# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ipcms', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='temppatientdata',
            old_name='dob',
            new_name='DOB',
        ),
        migrations.AddField(
            model_name='temppatientdata',
            name='address',
            field=models.CharField(max_length=256, default=''),
        ),
        migrations.AddField(
            model_name='temppatientdata',
            name='insurance_policy_number',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='temppatientdata',
            name='insurance_provider',
            field=models.CharField(max_length=256, default=''),
        ),
    ]
