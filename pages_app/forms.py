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
        fields = ('title', 'subtitle', 'body', 'date', 'author', 'image')
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

class UserRegisterForm(UserCreationForm):
    password1: forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2: forms.CharField(label='Repetir contraseña', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']
        widgets = {
            
            'first_name':forms.TextInput(attrs={'class':'form-control'}),
            'last_name':forms.TextInput(attrs={'class':'form-control'}),
            'username':forms.TextInput(attrs={'class':'form-control'}),
            'email':forms.EmailInput(attrs={'class':'form-control'}),
            'password1':forms.PasswordInput(attrs={'class':'form-control'}),
            'password2':forms.PasswordInput(attrs={'class':'form-control'}),
                
        }