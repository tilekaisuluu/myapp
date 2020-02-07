from django.http import HttpResponse
from .models import Medication, SideEffect
from django.shortcuts import render
from django.db.models import Q


def list(request):
   print('inside list function')
   medication_list = Medication.objects.all()
   side_effect_list = SideEffect.objects.all()
   return render(request, 'drugs/list.html', {'medication_list':medication_list,
                                               'side_effect_list':side_effect_list})



def search(request):
    # check if query is get request
    if 'query' in request.GET:
        # extract search term from request
        query = request.GET['query']

        # empty list for all results
        search_results_list = []

        # filtering medication names
        result = Medication.objects.filter(Q(medication_name__icontains=query))
        # adding medication name results to search_results_list
        for m in result:
            # adding all medications which related to side effect which is found to search_results_list
            search_results_list.append(m)

        # filtering side effects
        result2 = SideEffect.objects.filter(Q(side_effect__icontains=query))
        # loop through each side effect in result2
        for se in result2:
            # adding all medications which related to side effect which is found to search_results_list
            search_results_list.append(se.medication)
        # rendering to the list.html page

        print('results %s' % search_results_list)
        return render(request, 'drugs/list.html', {'search_results_list': search_results_list})
     # if not render to search.html page

    else:
        print('rendering search.html')
        return render(request, 'drugs/search.html')

        # IF THIS IS A GET:
        # render search.html

        # IF THIS IS A POST:
        # https://docs.djangoproject.com/en/3.0/intro/tutorial04/

        # extract search term from POST request (ex: https://stackoverflow.com/questions/39842386/django-simple-search-form)

        # search_results_list = []

        # 1 search:
        # res = Medication.objects.filter(medication_name=medication.medication_name)
        # add results to search_results_list

        # 2 search:
        # res2 = SideEffect.objects.filter()

        # find all medications for the side effects that you found
        # for se in res2:
        # search_results_list.append(se.medication)

        # return render (... search_results_list ...

    # if it is a GET render search.html
    #return render(request, 'drugs/list.html', {'medication_list':medication_list,
    #                                          'side_effect_list':side_effect_list})