from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


class Link(models.Model):
    short_link = models.SlugField('Сокращенная ссылка', max_length=50, unique=True)
    long_link = models.CharField('Длинная ссылка', max_length=250)
    desc = models.TextField('Описание ссылки', default='Полное описание сайта')
    author = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='Автор ссылки')

    def __str__(self):
        return self.short_link

    def get_absolute_url(self):
        return reverse('link')
