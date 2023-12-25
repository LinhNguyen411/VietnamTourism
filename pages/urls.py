from django.urls import path
from . import views
urlpatterns = [
    path('', views.HomePageView.as_view(), name='home'),

    path('vietnam/', views.VietNamView.as_view(), name='vietnam'),
    path('vietnam/<str:region>/', views.RegionDetailView, name='region-detail'),
    path('vietnam/<str:region>/<str:city>/', views.CityDetailView, name='city-detail'),
    path('vietnam/<str:region>/<str:city>/<str:destination>/', views.DestinationDetailView, name='destination-detail'),

    path('search/', views.SearchView.as_view(), name = 'search'),
]
