from django.http import HttpResponse, Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.http import Http404
from django.utils.timezone import utc, get_default_timezone
from django.contrib.auth.decorators import permission_required
from django.template import Context, Template
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.shortcuts import get_object_or_404
from django.views.decorators.csrf import csrf_exempt
import json

from network.models import Chapter, Recruit, RushChair

from sms import sendSMS

def logIn(request):
    if request.method == 'GET':
        return render(request, 'logIn.html')
    else:
        username = request.POST['email']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                print "# Redirect to a success page."
            else:
                print "# Return a 'disabled account' error message"
        else:
            print "# Return an 'invalid login' error message."

        return redirect('/')

def logOut(request):
    logout(request)
    return redirect('/')

def home(request):
    params = {'tab1': 'active'}
    if request.user.is_authenticated() and request.user.isRushChair():
        params['isRushChair'] = True
    return render(request, 'greekpeek.html', params)

def rushAdmin(request):
    if not request.user.isRushChair():
        return redirect('/')
    params = {'tab4': 'active'}
    rushChair = RushChair.objects.get(user=request.user)
    params['rushing'] = rushChair.chapter.recruit_set.all()
    if request.user.is_authenticated() and request.user.isRushChair():
            params['isRushChair'] = True
    if request.method == 'GET':
        rushChair = RushChair.objects.get(user=request.user)
        params['rushing'] = rushChair.chapter.recruit_set.all()
        params['chapter'] = rushChair.chapter
        return render(request, 'blast.html', params)
    else:
        textBody = request.POST.get('text')
        receivers = request.POST.getlist('receivers[]')
        print "Text: %s" % textBody
        for pk in receivers:
            recruit = Recruit.objects.get(pk=pk)
            print 'Texting "%s" at %s' % (recruit.user, recruit.phone)
            if recruit.phone:
                sendSMS(recruit.phone, textBody)
        return render(request, 'blast.html', params)

def whyJoin(request):
    params = {'tab3': 'active'}
    if request.user.is_authenticated() and request.user.isRushChair():
        params['isRushChair'] = True
    return render(request, 'whyjoin.html', params)

def signUp(request):
    print request.method
    if request.method == "GET":
        return render(request, 'member-signup.html')
    elif request.method == "POST":
        pwd1 = request.POST.get('password1')
        pwd2 = request.POST.get('password2')
        lastName = request.POST.get('last-name')
        firstName = request.POST.get('first-name')
        grade = request.POST.get('grade')
        email = request.POST.get('email')
        phone = request.POST.get('phone-number')

        user = get_user_model().objects.create_user(email, pwd1)
        user.firstName = firstName
        user.lastName = lastName
        user.save()

        recruit = Recruit()
        recruit.user = user
        recruit.phone = phone
        recruit.grade = grade
        recruit.save()

        user = authenticate(username=email, password=pwd1)
        if user is not None:
            if user.is_active:
                login(request, user)
                return redirect('/')
                print "# Redirect to a success page."
            else:
                print "# Return a 'disabled account' error message"
        else:
            print "# Return an 'invalid login' error message."

        return HttpResponse('firstName')

def fraternities(request):
    params = {'tab2': 'active'}
    if request.user.is_authenticated() and request.user.isRushChair():
        params['isRushChair'] = True

    if request.user.is_authenticated() and request.user.isRecruit():
        recruit = Recruit.objects.get(user=request.user)
        params['rushing'] = recruit.houses.all()
    if request.method == 'GET':
        return render(request, 'fraternities.html', params)
    else:
        action = str(request.POST.get('action'))
        for key in request.POST:
            if key in ['csrfmiddlewaretoken', 'action']: continue
            chapter = Chapter.objects.get(name=key) #Official English Name
            recruit = Recruit.objects.get(user=request.user)
            if action == 'Subscribe to SMS updates':
                recruit.subscribe(chapter)
            elif action == 'Unsubscribe from SMS updates':
                recruit.unsubscribe(chapter)    
        return render(request, 'fraternities.html', params)

def contactUs(request):
    return render(request, 'contactUs.html')

def policies(request):
    return render(request, 'policies.html')

def formComplete(request):
    return render(request, 'formComplete.html')

def jsonID(request, num):
    return HttpResponse(num)

@csrf_exempt
def ajax(request, chapter):
    chapter = get_object_or_404(Chapter, name=chapter)
    recruits = chapter.recruit_set.all()
    compilation = []
    for recruit in recruits:
        data = {
            'firstName': recruit.user.firstName,
            'lastName': recruit.user.lastName,
            'email': recruit.user.email,
            'grade': recruit.grade,
            'phone': recruit.phone,
            'major': recruit.major,
            'bio': recruit.bio 
        }
        compilation.append(data)
    serialized = json.dumps(compilation)
    return HttpResponse(serialized, content_type="application/json")

def namesTest(request):
    return render(request, 'names.html')

def profileSettings(request):
    params = {}
    if request.user.is_authenticated() and request.user.isRecruit():
        params['recruit'] = get_object_or_404(Recruit, user=request.user)
    if request.user.is_authenticated() and request.user.isRushChair():
        params['isRushChair'] = True
    if request.method == 'POST':
        print "method1"        
        print request.POST
        user = request.user
        #user = get_user_model().objects.get(user=request.user)
        recruit = Recruit.objects.get(user=user)
        bio = request.POST.get('bio')
        lastName = request.POST.get('last-name')
        firstName = request.POST.get('first-name')
        email = request.POST.get('email') 
        phone = request.POST.get('phone-number')
        grade = request.POST.get('grade')
        major = request.POST.get('major')

        user.firstName = firstName
        user.lastName = lastName
        user.email = email
        recruit.phone = phone
        recruit.grade = grade
        recruit.major = major
        recruit.bio = bio
        recruit.save()
        user.save()

        return redirect('/profileSettings')
    return render(request, 'profileSettings.html', params)

def profileSettings2(request):
    params = {}
    if request.user.is_authenticated() and request.user.isRecruit():
        params['recruit'] = get_object_or_404(Recruit, user=request.user)
    if request.method == 'POST':
        print "method2"        
        print request.POST
        #return redirect('/profileSettings')
    return render(request, 'profileSettings.html', params)
