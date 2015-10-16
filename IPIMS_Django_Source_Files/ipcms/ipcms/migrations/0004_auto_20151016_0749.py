# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        ('ipcms', '0003_remove_patient_role'),
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
            field=models.CharField(max_length=256, default='Select Doctor Type', choices=[('Gynecologist', 'Gynecologist'), ('Neuro', 'Neuro')]),
        ),
        migrations.AlterField(
            model_name='patient',
            name='fill_from_application',
            field=models.ForeignKey(unique=True, to='ipcms.TempPatientData', null=True, default=''),
        ),
        migrations.AlterField(
            model_name='patient',
            name='user',
            field=models.OneToOneField(blank=True, to=settings.AUTH_USER_MODEL, null=True, default=''),
        ),
        migrations.AlterField(
            model_name='patientappt',
            name='allergies',
            field=models.CharField(max_length=1000, default='None'),
        ),
        migrations.AlterField(
            model_name='patientappt',
            name='current_health_conditions',
            field=models.ForeignKey(blank=True, to='ipcms.PatientHealthConditions', null=True, default=''),
        ),
        migrations.AlterField(
            model_name='patientappt',
            name='medical_conditions',
            field=models.CharField(max_length=1000, default='None'),
        ),
        migrations.AlterField(
            model_name='patientappt',
            name='user',
            field=models.ForeignKey(blank=True, to='ipcms.Patient', default=''),
        ),
        migrations.AlterField(
            model_name='patienthealthconditions',
            name='user',
            field=models.ForeignKey(blank=True, to='ipcms.Patient', default=''),
        ),
        migrations.AlterField(
            model_name='permissionsrole',
            name='role',
            field=models.CharField(max_length=256, choices=[('admin', 'admin'), ('nurse', 'nurse'), ('staff', 'staff'), ('doctor', 'doctor'), ('patient', 'patient'), ('lab', 'lab')]),
        ),
        migrations.AlterField(
            model_name='permissionsrole',
            name='user',
            field=models.OneToOneField(blank=True, to=settings.AUTH_USER_MODEL, default=''),
        ),
        migrations.AlterField(
            model_name='temppatientdata',
            name='address',
            field=models.CharField(max_length=256, default=''),
        ),
        migrations.AlterField(
            model_name='temppatientdata',
            name='allergies',
            field=models.CharField(max_length=256, default=''),
        ),
        migrations.AlterField(
            model_name='temppatientdata',
            name='first_name',
            field=models.CharField(max_length=256, default=''),
        ),
        migrations.AlterField(
            model_name='temppatientdata',
            name='insurance_provider',
            field=models.CharField(max_length=256, default=''),
        ),
        migrations.AlterField(
            model_name='temppatientdata',
            name='last_name',
            field=models.CharField(max_length=256, default=''),
        ),
        migrations.AlterField(
            model_name='temppatientdata',
            name='medications',
            field=models.CharField(max_length=256, default=''),
        ),
        migrations.AlterField(
            model_name='temppatientdata',
            name='user',
            field=models.ForeignKey(unique=True, to=settings.AUTH_USER_MODEL, null=True, default=''),
        ),
    ]
