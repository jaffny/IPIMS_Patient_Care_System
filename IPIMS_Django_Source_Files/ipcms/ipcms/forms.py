from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import *
from .models import Patient, PatientAppt, TempPatientData
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
        fields = ['phone_number', 'email_address', 'user']


class PatientApptForm(forms.ModelForm):
    class Meta:
        model = PatientAppt
        widgets = {
        'date': forms.TextInput(attrs={'placeholder': 'Example: Oct. 10, 2015, 10:10 p.m.'}),
    }
        fields = '__all__'
        exclude = ['user']
        # exclude = ['user']
class PatientDataForm(forms.ModelForm):
    class Meta:
        model = TempPatientData
        fields = '__all__'
        exclude = ['user']
