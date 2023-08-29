from django import forms
from django.forms import ModelForm

from .models import *

class TaskForm(forms.ModelForm):
    Add_New_Task=forms.CharField(widget=forms.TextInput(attrs={'placeholder': 'Add New Task Here'}))
    class Meta:
        model=Task
        fields = '__all__'