from django import forms
from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'subtitle', 'body', 'date', 'author')
        widgets = {
            'author':forms.Select(attrs={'class': 'form-author'}),
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'subtitle':forms.TextInput(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
            'date':forms.SelectDateWidget(attrs={'class':'form-date'}),
                
        }


class PostFormUpdate(forms.ModelForm):
    class Meta:
        model = Post
        fields = ('title', 'subtitle', 'body', 'date')
        widgets = {
            
            'title':forms.TextInput(attrs={'class':'form-control'}),
            'subtitle':forms.TextInput(attrs={'class':'form-control'}),
            'body':forms.Textarea(attrs={'class':'form-control'}),
            'date':forms.SelectDateWidget(attrs={'class':'form-date'}),
                
        }