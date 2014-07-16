from django.shortcuts import render
from network.choices import states
from network.models import Campus

def index(request):
    return render(request, 'home.html')

def campusSelection(request):
    params = {}
    stateMap = {}
    for abbrv, full in states:
        stateMap[full] = Campus.objects.filter(state=abbrv)    
    params['states'] = stateMap
    print stateMap
    return render(request, 'campus.html', params)
