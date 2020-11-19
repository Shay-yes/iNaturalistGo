from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


# form for user to register
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# form for user to login
class UserLoginForm(forms.Form):
    user_name = forms.CharField(label='username', max_length=100)
    pass_word = forms.CharField(label='password', max_length=100, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username', 'password']
