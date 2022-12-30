from django.urls import path

from .views import ClothListView, ClothDetailView, SearchResultsListView

urlpatterns = [
    path('', ClothListView.as_view(), name='cloth_list'),
    path('<uuid:pk>', ClothDetailView.as_view(), name='cloth_detail'),
    path('search/', SearchResultsListView.as_view(), name='search_results'),
]
