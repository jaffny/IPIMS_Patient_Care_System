# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings
import django.core.validators
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Doctor',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('doctor_first_name', models.CharField(max_length=256, default='')),
                ('doctor_last_name', models.CharField(max_length=256, default='')),
                ('doctor_type', models.CharField(choices=[('Gynecologist', 'Gynecologist'), ('Neuro', 'Neuro')], max_length=256, default='Select Doctor Type')),
            ],
        ),
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, blank=True)),
                ('email_address', models.EmailField(max_length=254, blank=True)),
                ('approved', models.IntegerField(default=0)),
                ('user', models.OneToOneField(default='', to=settings.AUTH_USER_MODEL, null=True, blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='PatientAppt',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('date', models.DateTimeField(unique=True)),
                ('pain_level', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], default=0)),
                ('medical_conditions', models.CharField(max_length=1000, default='None')),
                ('allergies', models.CharField(max_length=1000, default='None')),
                ('nausea_level', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], default=0)),
                ('hunger_level', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], default=0)),
                ('anxiety_level', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], default=0)),
                ('stomach_level', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], default=0)),
                ('body_ache_level', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], default=0)),
                ('chest_pain_level', models.IntegerField(validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(10)], default=0)),
                ('doctor', models.ForeignKey(to='ipcms.Doctor', default='Select A Doctor..')),
                ('user', models.ForeignKey(to='ipcms.Patient', blank=True, default='')),
            ],
        ),
        migrations.CreateModel(
            name='PermissionsRole',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('role', models.CharField(choices=[('admin', 'admin'), ('nurse', 'nurse'), ('staff', 'staff'), ('doctor', 'doctor'), ('patient', 'patient'), ('lab', 'lab')], max_length=256)),
                ('user', models.OneToOneField(to=settings.AUTH_USER_MODEL, default='', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='TempPatientData',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=256, default='')),
                ('last_name', models.CharField(max_length=256, default='')),
                ('phone_number', phonenumber_field.modelfields.PhoneNumberField(max_length=128, blank=True)),
                ('dob', models.IntegerField(default=0)),
                ('ssn', models.IntegerField(default=0)),
                ('allergies', models.CharField(max_length=256, default='')),
                ('medications', models.CharField(max_length=256, default='')),
                ('user', models.ForeignKey(to='ipcms.Patient', null=True)),
            ],
        ),
    ]
