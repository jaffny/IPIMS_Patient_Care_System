# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ipcms', '0021_auto_20151010_1744'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='patient',
            name='user_role',
        ),
        migrations.AddField(
            model_name='patient',
            name='user',
            field=models.OneToOneField(null=True, default=b'', blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
