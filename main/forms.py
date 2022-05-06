from django.forms import ValidationError, forms, ModelForm
from main.models import Manna, Comment, User
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.forms import UserCreationForm


class MannaForm(ModelForm):
    class Meta:
        model = Manna
        exclude = ['user','slug', 'created','updated']



    def keyverses_clean(self):
        data = self.cleaned_data.get('keyverses')
        
        if ':' not in data:
            raise ValidationError(_('key verses refers to pages in the bible, so must contain ":"'), code='Invalid')
        return data


class RegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email','first_name','last_name','username','password1','password2',]