from django.http import HttpResponse
from .models import Medication, SideEffect
from django.shortcuts import render
from django.views import generic
from django.views.generic import ListView, DetailView


def list(request):
   print('inside list function')
   medication_list = Medication.objects.all()
   side_effect_list = SideEffect.objects.all()
   #for med in medication_list:
    #   print(med.medication_name)
     #  for med.medication_name in medication_list:
      #     print(med.sideeffect_set.all())


   return render(request, 'drugs/list.html', {'medication_list':medication_list,
                                               'side_effect_list':side_effect_list})


# class MedicationDetailView(DetailView):
#     model = Medication
#     template_name = 'drugs/medication_detail.html
