from operator import is_
from django.shortcuts import render, redirect
from pages_app.models import Post
from .forms import PostForm, PostFormUpdate, UserRegisterForm
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.urls import reverse

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LogoutView



def Home (request):
    return render(request, 'pages_app/home.html')

def About (request):
    return render(request, 'pages_app/about_us.html')

class Page_view(ListView):
    model = Post
    template = 'post_list.html'

class Page_create(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template = 'post_form.html'
    #fields ='__all__'

class Page_article(DetailView):
    model = Post
    template = 'post_detail.html'

class Page_update(LoginRequiredMixin, UpdateView):
    model = Post
    form_class = PostFormUpdate
    template = 'post_update.html'
    #fields = ['title', 'subtitle', 'body', 'date']

@login_required
def delete_post(request, pk):
    post = Post.objects.get(id=pk)
    delete_id = post.id
    post.delete()
    back_url = f"{reverse('home_post')}?borrado={delete_id}"

    return redirect(back_url)

def register(request):
    form_class = UserRegisterForm
    mensaje = ''
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)

        if form.is_valid():
            form.save()
            return render(request, "pages_app/home.html" , {"mensaje": "Usuario Creado: "})
        else:
            mensaje = 'Error en datos ingresados'
    form = UserRegisterForm()
    context = {"form": form, "mensaje": mensaje}
    
    return render(request, "pages_app/register.html", context=context)

def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data= request.POST)

        if form.is_valid():
            usuario = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=usuario, password=password)

            if user:
                login(request, user)
                return render(request, "pages_app/home.html" , {"mensaje":f"Bienvenido {usuario}"})
            else:
                 return render(request, "pages_app/login.html" , {"mensaje": "Error en datos ingresados"})
        else:
            return render(request, "pages_app/login.html" , {"mensaje": "Error en datos ingresados"})
    form = AuthenticationForm()
    return render(request, "pages_app/login.html", {'form':form})


class CustomLogoutView(LogoutView):
    template_name = 'pages_app/logout.html'