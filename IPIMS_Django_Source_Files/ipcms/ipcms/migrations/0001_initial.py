# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
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
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('doctor_first_name', models.CharField(default='', max_length=256)),
                ('doctor_last_name', models.CharField(default='', max_length=256)),
                ('doctor_type', models.CharField(default='Select Doctor Type', max_length=256, choices=[('Gynecologist', 'Gynecologist'), ('Neuro', 'Neuro')])),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128)),
                ('email_address', models.EmailField(blank=True, max_length=254)),
                ('approved', models.IntegerField(default=0)),
                ('user', models.OneToOneField(blank=True, null=True, default='', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PatientAppt',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(unique=True)),
                ('pain_level', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('medical_conditions', models.CharField(default='None', max_length=1000)),
                ('allergies', models.CharField(default='None', max_length=1000)),
                ('nausea_level', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('hunger_level', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('anxiety_level', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('stomach_level', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('body_ache_level', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('chest_pain_level', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)])),
                ('doctor', models.ForeignKey(default='Select A Doctor..', to='ipcms.Doctor')),
                ('user', models.ForeignKey(blank=True, default='', to='ipcms.Patient')),
            ],
        ),
        migrations.CreateModel(
            name='PermissionsRole',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('role', models.CharField(max_length=256, choices=[('admin', 'admin'), ('nurse', 'nurse'), ('staff', 'staff'), ('doctor', 'doctor'), ('patient', 'patient'), ('lab', 'lab')])),
                ('user', models.OneToOneField(blank=True, default='', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='TempPatientData',
            fields=[
                ('id', models.AutoField(primary_key=True, auto_created=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(default='', max_length=256)),
                ('last_name', models.CharField(default='', max_length=256)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128)),
                ('DOB', models.IntegerField(default=0)),
                ('ssn', models.IntegerField(default=0)),
                ('allergies', models.CharField(default='', max_length=256)),
                ('address', models.CharField(default='', max_length=256)),
                ('medications', models.CharField(default='', max_length=256)),
                ('insurance_provider', models.CharField(default='', max_length=256)),
                ('insurance_policy_number', models.IntegerField(default=0)),
                ('user', models.ForeignKey(default='Select a patient', null=True, unique=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
