# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ipcms', '0003_auto_20151009_2019'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientappt',
            name='user',
            field=models.OneToOneField(default=b'', blank=True, to='ipcms.Patient'),
        ),
        migrations.AddField(
            model_name='permissionsroles',
            name='user',
            field=models.OneToOneField(default=b'', blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='patient',
            name='user',
            field=models.OneToOneField(default=b'', blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
