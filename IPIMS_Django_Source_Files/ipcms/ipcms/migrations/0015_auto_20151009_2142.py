# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        ('ipcms', '0014_auto_20151009_2134'),
    ]

    operations = [
        migrations.AddField(
            model_name='patientappt',
            name='allergies',
            field=models.CharField(default=b'None', max_length=1000),
        ),
        migrations.AddField(
            model_name='patientappt',
            name='anxiety_level',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AddField(
            model_name='patientappt',
            name='body_ache_level',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AddField(
            model_name='patientappt',
            name='chest_pain_level',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AddField(
            model_name='patientappt',
            name='hunger_level',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AddField(
            model_name='patientappt',
            name='medical_conditions',
            field=models.CharField(default=b'None', max_length=1000),
        ),
        migrations.AddField(
            model_name='patientappt',
            name='nausea_level',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AddField(
            model_name='patientappt',
            name='stomach_level',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)]),
        ),
        migrations.AlterField(
            model_name='patientappt',
            name='date',
            field=models.DateTimeField(unique=True),
        ),
    ]
