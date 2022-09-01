from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import ValidationError
from django.utils.translation import gettext_lazy as _

from finance_app.models import Income, IncomeInstance


def validate_income(income,description):
    income = IncomeInstance.objects.filter(income = income,description=description)
    if income:
        raise ValidationError(
            _('%(value)s already exists, if you wish to update please click on edit'),
            params={'value': description},
        )


class UserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username', 'email')
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'John'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Doe'}),
            'username': forms.TextInput(attrs={'class': 'form-control', 'aria-describedby': 'inputGroupPrepend', 'placeholder': 'JohnDoe'}),
            'email': forms.TextInput(attrs={'type': 'email', 'class': 'form-control'}),
        }


class LoginForm(forms.Form):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control', 'aria-describedby': 'emailHelp', 'placeholder': 'JohnDoe'}), help_text="Your profile username")
    password = forms.CharField(widget=forms.TextInput(
        attrs={'type': 'password', 'class': 'form-control', 'aria-describedby': 'passHelp'}))


class IncomeInstanceForm(forms.ModelForm):
    
    class Meta:
        
        model = IncomeInstance
        exclude = ['income']
        widgets = {
            'description': forms.TextInput(attrs={"type":"text","class":"form-control","id":"description","placeholder":"Description"}),
            'amount': forms.TextInput(attrs={"type":"number","class":"form-control","id":"amount","placeholder":"Amount Per Year"}),
            'age_start': forms.TextInput(attrs={"type":"number","class":"form-control","id":"start","placeholder":"Age at Start"}),
            'age_stop': forms.TextInput(attrs={"type":"number","class":"form-control","id":"stop","placeholder":"Age at End"}),
            'growth': forms.TextInput(attrs={"type":"number","class":"form-control","id":"growth","placeholder":"Amount Per Year"}),
        }

