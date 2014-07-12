from django.shortcuts import render

def index(request):
    return render(request, 'index.html')

def campusSelection(request):

    return render(request, 'campus.html')
