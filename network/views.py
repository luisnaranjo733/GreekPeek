from django.shortcuts import render, redirect, get_object_or_404
from network.choices import states
from network.models import Campus

def index(request):
    return render(request, 'home.html')

def campusSelection(request):
    if request.method == 'POST' and request.user.is_authenticated:
        campusName = request.POST.get('campus')
        if campusName:
            campus = get_object_or_404(Campus, name=campusName)
            request.user.campus = campus
            request.user.save()
            print campus.pk
    params = {}
    stateMap = {}
    for abbrv, full in states:
        stateMap[full] = Campus.objects.filter(state=abbrv)    
    params['states'] = stateMap
    return render(request, 'campus.html', params)

def userProfile(request, pk):

    params = {}
    return render(request, 'userProfile.html', params)
