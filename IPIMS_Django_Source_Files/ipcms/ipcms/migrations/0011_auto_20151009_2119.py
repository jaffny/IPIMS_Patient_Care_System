# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('ipcms', '0010_patient_email_address'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientappt',
            name='pain_level',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='patientappt',
            name='user',
            field=models.ForeignKey(default=b'', blank=True, to='ipcms.Patient'),
        ),
    ]
