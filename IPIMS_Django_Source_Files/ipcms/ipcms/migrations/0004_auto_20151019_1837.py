# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipcms', '0003_remove_patient_role'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alert',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('alert_level', models.IntegerField(default=0)),
                ('alert_description', models.CharField(default=b'', max_length=255, null=True)),
            ],
        ),
        migrations.AddField(
            model_name='patient',
            name='alertSent',
            field=models.IntegerField(default=0),
        ),
        migrations.AddField(
            model_name='alert',
            name='alert_patient',
            field=models.OneToOneField(to='ipcms.Patient'),
        ),
    ]
