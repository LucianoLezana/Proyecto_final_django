from django.shortcuts import render, redirect
from pages_app.models import Post
from .forms import PostForm, PostFormUpdate
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse


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


def delete_post(request, pk):
    post = Post.objects.get(id=pk)
    delete_id = post.id
    post.delete()
    back_url = f"{reverse('home_post')}?borrado={delete_id}"

    return redirect(back_url)


