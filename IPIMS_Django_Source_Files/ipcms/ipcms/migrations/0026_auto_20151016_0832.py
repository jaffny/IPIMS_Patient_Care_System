# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('ipcms', '0025_auto_20151010_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='doctor_first_name',
            field=models.CharField(max_length=256, default=''),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='doctor_last_name',
            field=models.CharField(max_length=256, default=''),
        ),
        migrations.AlterField(
            model_name='doctor',
            name='doctor_type',
            field=models.CharField(choices=[('Gynecologist', 'Gynecologist'), ('Neuro', 'Neuro')], max_length=256, default='Select Doctor Type'),
        ),
        migrations.AlterField(
            model_name='patient',
            name='user',
            field=models.OneToOneField(null=True, to=settings.AUTH_USER_MODEL, default='', blank=True),
        ),
        migrations.AlterField(
            model_name='patientappt',
            name='allergies',
            field=models.CharField(max_length=1000, default='None'),
        ),
        migrations.AlterField(
            model_name='patientappt',
            name='doctor',
            field=models.ForeignKey(default='Select A Doctor..', to='ipcms.Doctor'),
        ),
        migrations.AlterField(
            model_name='patientappt',
            name='medical_conditions',
            field=models.CharField(max_length=1000, default='None'),
        ),
        migrations.AlterField(
            model_name='patientappt',
            name='user',
            field=models.ForeignKey(to='ipcms.Patient', default='', blank=True),
        ),
        migrations.AlterField(
            model_name='permissionsrole',
            name='role',
            field=models.CharField(choices=[('admin', 'admin'), ('nurse', 'nurse'), ('staff', 'staff'), ('doctor', 'doctor'), ('patient', 'patient'), ('lab', 'lab')], max_length=256),
        ),
        migrations.AlterField(
            model_name='permissionsrole',
            name='user',
            field=models.OneToOneField(to=settings.AUTH_USER_MODEL, default='', blank=True),
        ),
    ]
