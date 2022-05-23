from django.forms import ValidationError, forms, ModelForm
from main.models import Manna, Comment, User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm, PasswordResetForm


class MannaForm(ModelForm):
    class Meta:
        model = Manna
        exclude = ['user', 'slug', 'created', 'updated', 'display_verse']


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name', 'username', 'password1', 'password2', ]



