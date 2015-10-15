# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import phonenumber_field.modelfields
from django.conf import settings
import django.core.validators


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('doctor_first_name', models.CharField(default=b'', max_length=256)),
                ('doctor_last_name', models.CharField(default=b'', max_length=256)),
                ('doctor_type', models.CharField(default=b'Select Doctor Type', max_length=256, choices=[(b'Gynecologist', b'Gynecologist'), (b'Neuro', b'Neuro')])),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('approved', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='PatientAppt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.CharField(unique=True, max_length=1000)),
                ('pain_level', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('medical_conditions', models.CharField(default=b'None', max_length=1000)),
                ('allergies', models.CharField(default=b'None', max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='PatientHealthConditions',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nausea_level', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('hunger_level', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('anxiety_level', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('stomach_level', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('body_ache_level', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('chest_pain_level', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('user', models.ForeignKey(default=b'', blank=True, to='ipcms.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='PermissionsRole',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role', models.CharField(max_length=256, choices=[(b'admin', b'admin'), (b'nurse', b'nurse'), (b'staff', b'staff'), (b'doctor', b'doctor'), (b'patient', b'patient'), (b'lab', b'lab')])),
                ('user', models.OneToOneField(default=b'', blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TempPatientData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(default=b'', max_length=256)),
                ('last_name', models.CharField(default=b'', max_length=256)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, blank=True)),
                ('DOB', models.IntegerField(default=0)),
                ('ssn', models.IntegerField(default=0)),
                ('allergies', models.CharField(default=b'', max_length=256)),
                ('address', models.CharField(default=b'', max_length=256)),
                ('medications', models.CharField(default=b'', max_length=256)),
                ('insurance_provider', models.CharField(default=b'', max_length=256)),
                ('insurance_policy_number', models.IntegerField(default=0)),
                ('email_address', models.CharField(unique=True, max_length=500)),
                ('data_sent', models.IntegerField(default=0)),
                ('user', models.ForeignKey(null=True, default=b'', to=settings.AUTH_USER_MODEL, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='patientappt',
            name='current_health_conditions',
            field=models.ForeignKey(default=b'', blank=True, to='ipcms.PatientHealthConditions', null=True),
        ),
        migrations.AddField(
            model_name='patientappt',
            name='doctor',
            field=models.ForeignKey(default=-1, to='ipcms.Doctor'),
        ),
        migrations.AddField(
            model_name='patientappt',
            name='user',
            field=models.ForeignKey(default=b'', blank=True, to='ipcms.Patient'),
        ),
        migrations.AddField(
            model_name='patient',
            name='fill_from_application',
            field=models.ForeignKey(null=True, default=b'', to='ipcms.TempPatientData', unique=True),
        ),
        migrations.AddField(
            model_name='patient',
            name='role',
            field=models.OneToOneField(default=4, to='ipcms.PermissionsRole'),
        ),
        migrations.AddField(
            model_name='patient',
            name='user',
            field=models.OneToOneField(null=True, default=b'', blank=True, to=settings.AUTH_USER_MODEL),
        ),
    ]
