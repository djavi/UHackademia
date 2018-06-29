from django.contrib.auth.models import User, Group
from django.forms import modelformset_factory
from django.db.models import Q
from .models import *

from django import forms
class login(forms.ModelForm):

    class Meta:

        model = User
        fields = ['username','password']

        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username...'}),
            'password':forms.PasswordInput(attrs={'placeholder': 'Password...'}),
        }


class register(forms.ModelForm):

    class Meta:

        model = UserDetail
        fields = ['user','firstName','lastName','address','contactNum']
