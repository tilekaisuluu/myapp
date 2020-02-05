from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.MedicationListView.as_view(), name='list' ),
    path('<int:pk>/detail/', views.MedicationDetailView.as_view(), name='detail'),

]