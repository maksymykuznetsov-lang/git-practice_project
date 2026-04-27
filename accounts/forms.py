from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

# Форма реєстрації
class UserRegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'username')
        labels = {
            'username': 'Логін:',
            'first_name': 'Ім\'я:',
            'last_name': 'Прізвище:',
        }

# Форма входу
class UserLoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ('username', 'password')