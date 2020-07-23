from django import forms
from .models import Todo

class Todoform(forms.Form):
    text = forms.CharField(max_length=40, widget=forms.TextInput(
        attrs={'class': 'form-control', 'placeholder': 'Enter Todo e.g. Delete junk files'}))

class Newtodoform(forms.ModelForm):
    class Meta():
        model = Todo
        fields = ['text']
        widgets = {
            'text': forms.TextInput(
                attrs={'class': 'form-control', 'placeholder': 'Enter Todo e.g. Delete junk files'})
        }
