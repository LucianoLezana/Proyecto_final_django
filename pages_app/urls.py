from django.urls import path
from pages_app import views
from .views import Page_create, Page_view, Page_article, Page_update

urlpatterns = [
    path('', views.Home, name="home"),
    path('about_us', views.About, name="about_us"),
    path('add_post/', Page_create.as_view(), name="add_post"),
    path('pages/', Page_view.as_view(), name="home_post"),
    path('pages/<int:pk>', Page_article.as_view(), name="article"),
    path('update_post/<int:pk>', Page_update.as_view(), name="update_post"),
    path('delete_post/<int:pk>', views.delete_post, name="delete_post"),
    path('register/', views.register, name="register"),
]