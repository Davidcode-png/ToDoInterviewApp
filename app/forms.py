from django.forms import forms
from .models import Item

from django.forms import ModelForm

class TaskForm(ModelForm):
    
    class Meta:
        model = Item
        fields = ("title","description","complete")
