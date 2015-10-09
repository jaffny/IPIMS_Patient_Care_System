# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipcms', '0009_auto_20151009_2059'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='email_address',
            field=models.EmailField(max_length=254, blank=True),
        ),
    ]
