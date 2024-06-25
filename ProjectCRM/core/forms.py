from django import forms
from .models import Records
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput


# Create User
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

# Login User
class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())


# Create a Record
class AddRecordForm(forms.ModelForm):
    class Meta:
        model = Records
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'city', 'state', 'country']