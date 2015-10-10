# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipcms', '0016_auto_20151010_0631'),
    ]

    operations = [
        migrations.AddField(
            model_name='patient',
            name='approved',
            field=models.IntegerField(default=0),
        ),
    ]
