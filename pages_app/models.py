from distutils.command.upload import upload
from email import contentmanager
from pyexpat import model
from unittest.util import _MAX_LENGTH
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from datetime import datetime
from ckeditor.fields import RichTextField

'''El Model Blog
Debe tener como mínimo los campos: título, subtítulo, cuerpo, autor, fecha y una imagen.
'''


class Post (models.Model):
    title = models.CharField(max_length=220)
    subtitle=models.CharField(max_length=220)
    body = RichTextField(blank=True, null=True)
    #body=models.TextField()
    author=models.ForeignKey(User, on_delete=models.CASCADE)
    date=models.DateTimeField(default=datetime.now, blank=True)
    image=models.ImageField(null=True, blank=True, upload_to="images/")

    def __str__(self):
        return f"{self.title} | fue creado por: {self.author} | {self.date}"

    def get_absolute_url(self):
        return reverse('article', args=(str(self.id)))

