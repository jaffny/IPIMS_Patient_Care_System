# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('ipcms', '0017_patient_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='patient',
            name='user',
            field=models.OneToOneField(related_name='email_address', null=True, default=b'', blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
