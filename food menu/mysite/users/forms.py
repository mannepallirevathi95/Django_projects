from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
# creation a new form by importing it and this form is for users and finally base coded part that to be inherited is also imported

# own form
# as in part of inheritence we pass base-coded class as a parameter to the new-class from
class RegisterForm(UserCreationForm):
    email = forms.EmailField()
    # defining a meta class for this form;
    # this class holds info of class : RegisterForm
    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'password2']
        