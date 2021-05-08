from django import forms
from django.core import validators
from app_two.models import User

class UserForm(forms.ModelForm):
    #first_name = forms.CharField()
    #last_name = forms.CharField()
    #email = forms.EmailField(validators=[validators.EmailValidator])
    class Meta():
        model = User
        fields = '__all__'