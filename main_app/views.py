from django.shortcuts import render, redirect
from django.views.generic.edit import CreateView, DeleteView
from django.views.generic import ListView
from .models import Wish


class WishList(ListView):
    model = Wish


class WishList(ListView):
    model = Wish


class WishCreateView(CreateView):
    model = Wish
    fields = ['description']


class WishDeleteView(DeleteView):
    model = Wish
    success_url = '/'
