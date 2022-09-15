from django.shortcuts import render
from pages_app.models import Post
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

def Home (request):
    return render(request, 'home.html')


class Page_view(ListView):
    model = Post
    template = 'post_list.html'


class Page_create(CreateView):
    model = Post
    template = 'post_form.html'
    fields ='__all__'


class Page_article(DetailView):
    model = Post
    template = 'post_detail.html'


class Page_update(UpdateView):
    model = Post
    template = 'post_update.html'
    fields = ['title', 'subtitle', 'body', 'date']


