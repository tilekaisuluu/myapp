from django.http import HttpResponse
from .models import Medication, SideEffect
from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView, DetailView

#
# class MedicationListView(ListView):
#     model = Medication
#     template_name = 'drugs/list.html'
#
#     def get_queryset(self):
#         medication_list = Medication.objects.all()
#         return medication_list


# class MedicationDetailView(DetailView):
#     model = Medication
#     template_name = 'drugs/medication_detail.html'


# class SideEffectListView(ListView):
#     model = SideEffect
#     template_name = 'drugs/list.html'
#
#     def get_queryset(self):
#         side_effect_list = SideEffect.objects.all()
#         return side_effect_list
#





def list(request):
   print('inside list function')
   medication_list = Medication.objects.all()
   side_effect_list = SideEffect.objects.all()

   return render(request, 'drugs/list.html', {'medication_list':medication_list,
                                               'side_effect_list':side_effect_list})