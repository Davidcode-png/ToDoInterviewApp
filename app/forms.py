from django.forms import forms
from .models import Item
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm
from django.contrib.auth.models import User

class TaskForm(ModelForm):
    
    class Meta:
        model = Item
        fields = ("title","description","complete")

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','email','username','password1','password2']
        labels = {
            'first_name':'Name'
        }


    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm,self).__init__(*args, **kwargs)
        self.fields['first_name'].widget.attrs.update({'class':'input100','placeholder':'Name'})
        self.fields['email'].widget.attrs.update({'class':'input100','placeholder':'Email'})
        self.fields['username'].widget.attrs.update({'class':'input100','placeholder':'Username'})
        self.fields['password1'].widget.attrs.update({'class':'input100','placeholder':'Password'})
        self.fields['password2'].widget.attrs.update({'class':'input100','placeholder':'Confirm Password'})