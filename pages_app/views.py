from django.shortcuts import render
from pages_app.models import Post
from .forms import PostForm, PostFormUpdate
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

def Home (request):
    return render(request, 'home.html')

def About (request):
    return render(request, 'about_us.html')

class Page_view(ListView):
    model = Post
    template = 'post_list.html'


class Page_create(CreateView):
    model = Post
    form_class = PostForm
    template = 'post_form.html'
    #fields ='__all__'


class Page_article(DetailView):
    model = Post
    template = 'post_detail.html'


class Page_update(UpdateView):
    model = Post
    form_class = PostFormUpdate
    template = 'post_update.html'
    #fields = ['title', 'subtitle', 'body', 'date']


