from email.policy import default
from pyexpat import model
from django import forms
from .models import Post
from datetime import datetime
from ckeditor.fields import RichTextField

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'subtitle', 'body', 'date', 'author')
        widgets = {
            'author':forms.Select(attrs={'class': 'form-author'}),
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'subtitle':forms.TextInput(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
            'date':forms.DateTimeInput(attrs={'class':'form-date'}),
                
        }


class PostFormUpdate(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'subtitle', 'body', 'date')
        widgets = {
            
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'subtitle':forms.TextInput(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
            'date':forms.DateTimeInput(attrs={'class':'form-date'}),
                
        }

class userRegisterForm(UserCreationForm):
    password1: forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2: forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']