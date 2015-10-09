# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('ipcms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='home_address',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='phone_numer',
        ),
        migrations.RemoveField(
            model_name='patient',
            name='url',
        ),
        migrations.AddField(
            model_name='patient',
            name='phone_number',
            field=phonenumber_field.modelfields.PhoneNumberField(max_length=128, blank=True),
        ),
    ]
