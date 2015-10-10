# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('ipcms', '0015_auto_20151009_2142'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='user',
            field=models.OneToOneField(null=True, default=b'', blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
