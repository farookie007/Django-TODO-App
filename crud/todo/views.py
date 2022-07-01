from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.shortcuts import render

from .models import TodoApp



# Create your views here.
class TodoAppCreateView(CreateView):
    model = TodoApp
    fields = [
        "title",
        "description"
    ]
    template_name = 'todo/home.html'
    success_url = reverse_lazy('todo:list')


class TodoAppListView(ListView):
    model = TodoApp
    template_name = 'todo/list.html'


class TodoAppDetailView(DetailView):
    model = TodoApp
    template_name = 'todo/detail.html'


class TodoAppUpdateView(UpdateView):
    model = TodoApp
    fields = [
        'title',
        'description'
    ]
    template_name = 'todo/update.html'
    success_url = reverse_lazy('todo:list')
