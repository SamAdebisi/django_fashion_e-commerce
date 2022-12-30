from django.db.models import Q
from django.contrib.auth.mixins import (
    LoginRequiredMixin,
    PermissionRequiredMixin
)
from django.views.generic import ListView, DetailView

from .models import Cloth


class ClothListView(LoginRequiredMixin, ListView):
    model = Cloth
    context_object_name = 'cloth_list'
    template_name = 'cloths/cloth_list.html'
    login_url = 'account_login'


class ClothDetailView(
    LoginRequiredMixin,
    PermissionRequiredMixin,
    DetailView
):
    model = Cloth
    context_object_name = 'cloth'
    template_name = 'cloths/cloth_detail.html'
    login_url = 'account_login'
    permission_required = 'cloths.special_status'


class SearchResultsListView(ListView):
    model = Cloth
    context_object_name = 'cloth_list'
    template_name = 'cloths/search_results.html'
    # queryset = Cloth.objects.filter(style__icontains='senator')

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Cloth.objects.filter(
            Q(style__icontains=query) | Q(stylist__icontains=query)
        )
