from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.list, name='list' ),
    path('search/', views.search, name='search'),
]