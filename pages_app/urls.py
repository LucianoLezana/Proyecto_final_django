from django.urls import path
from pages_app import views
from .views import Page_create, Page_view, Page_article, Page_update

urlpatterns = [
    path('', views.Home, name="home"),
    path('add_post/', Page_create.as_view(), name="add_post"),
    path('home_post/', Page_view.as_view(), name="home_post"),
    path('article/<int:pk>', Page_article.as_view(), name="article"),
    path('update_post/<int:pk>', Page_update.as_view(), name="update_post"),
]