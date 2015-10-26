# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipcms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='EMedication',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('medication_name', models.CharField(default=b'', max_length=255)),
                ('patient', models.OneToOneField(default=b'', to='ipcms.Patient')),
            ],
        ),
    ]
