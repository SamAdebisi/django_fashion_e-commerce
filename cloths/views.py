from django.shortcuts import render
from django.views.generic import ListView, DetailView

from .models import Cloth


class ClothListView(ListView):
    model = Cloth
    context_object_name = 'cloth_list'
    template_name = 'cloths/cloth_list.html'


class ClothDetailView(DetailView):
    model = Cloth
    context_object_name = 'cloth'
    template_name = 'cloths/cloth_detail.html'
