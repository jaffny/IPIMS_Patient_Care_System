# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('ipcms', '0004_auto_20151011_0255'),
    ]

    operations = [
        migrations.AlterField(
            model_name='temppatientdata',
            name='user',
            field=models.ForeignKey(default='Select a patient', null=True, unique=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
