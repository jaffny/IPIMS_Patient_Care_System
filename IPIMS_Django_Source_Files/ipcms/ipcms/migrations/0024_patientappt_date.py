# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import datetime
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('ipcms', '0023_remove_patientappt_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientappt',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2015, 10, 10, 22, 10, 46, 926736, tzinfo=utc), unique=True),
            preserve_default=False,
        ),
    ]
