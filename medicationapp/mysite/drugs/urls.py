from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.list, name='list' ),
    #path('<int:pk>/detail/', views.MedicationDetailView.as_view(), name='detail'),

]