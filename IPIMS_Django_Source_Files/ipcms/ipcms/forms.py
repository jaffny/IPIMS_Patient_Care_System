from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
from .models import Patient, PatientAppt, PatientHealthConditions, TempPatientData
from django.db import models
from django import forms

class RegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(RegistrationForm, self).__init__(*args, **kwargs)
        self.fields['username'].label = "Patient Email"
        self.helper = FormHelper()
        self.helper.layout = Layout(
            'username',
            'password1',
            'password2',
            ButtonHolder(
                Submit('register', 'Register', css_class='btn-primary')
            )
        )

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super(LoginForm, self).__init__(*args, **kwargs)

        self.helper = FormHelper()
        self.helper.layout = Layout(
            'username',
            'password',
            ButtonHolder(
                Submit('login', 'Login', css_class='btn-primary')
            )
        )

class PatientForm(forms.ModelForm):
    user = forms.CharField(max_length=40)
    class Meta:
        model = Patient
        fields = '__all__'


class PatientApptForm(forms.ModelForm):
    class Meta:
        model = PatientAppt
        widgets = {
        'date': forms.TextInput(attrs={'placeholder': 'Selecting This Textbox Will Enable A Drop Down For Date & Time'}),
    }
        fields = '__all__'
        exclude = ['user', 'current_health_conditions']


class PatientHealthConditionsForm(forms.ModelForm):
    class Meta:
        model = PatientHealthConditions
        fields = '__all__'
        exclude = ['user']


class TempPatientDataForm(forms.ModelForm):
    class Meta:
        model = TempPatientData
        fields = '__all__'
        exclude = ['user', 'data_sent']
