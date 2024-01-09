from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse
from django.views.generic import CreateView
from .models import Link
from django.shortcuts import render, redirect


def HomePage(request):
    return render(request, 'main/home.html', {'title': 'Главная страница'})


def AboutPage(request):
    return render(request, 'main/about.html', {'title': 'Про нас'})


class LinkAdd(LoginRequiredMixin, CreateView):
    model = Link
    template_name = 'main/link.html'

    fields = ['long_link', 'short_link']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super(LinkAdd, self).get_context_data(**kwargs)
        context['title'] = 'Добавить ссылку'
        links = Link.objects.filter(author=self.request.user)
        context['links'] = links
        return context

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)
