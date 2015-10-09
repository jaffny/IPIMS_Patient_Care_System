# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ipcms', '0011_auto_20151009_2119'),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('doctor_name', models.CharField(default=b'DEFAULT', max_length=256, choices=[(b'Dr. Schachte', b'Dr. Schachte'), (b'Dr. Schachte', b'Dr. Huffy')])),
            ],
        ),
    ]
