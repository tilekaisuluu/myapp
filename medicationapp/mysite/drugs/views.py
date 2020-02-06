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



def search(request):

    # IF THIS IS A GET:
            # render search.html

    # IF THIS IS A POST:
            # https://docs.djangoproject.com/en/3.0/intro/tutorial04/

            # extract search term from POST request (ex: https://stackoverflow.com/questions/39842386/django-simple-search-form)


            # search_results_list = []

            # 1 search:
            # res = Medication.objects.filter(....)
            # add results to search_results_list


            # 2 search:
            # res2 = SideEffect.objects.filter(....)

            # find all medications for the side effects that you found
            #for se in res2:
                #search_results_list.append(se.medication)

            # return render (... search_results_list ... )

           return render(request, 'drugs/list.html', {'medication_list':medication_list,
                                                       'side_effect_list':side_effect_list})