import os
import sys
from datetime import datetime
path = os.path.join('/home/luis/Dropbox/Greekpeek/', 'GreekPeek')
sys.path.append(path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'GreekPeek.settings'

from django.utils.timezone import utc
from django.contrib.auth.models import User
from django.template import Context, Template
from django.contrib.auth import get_user_model

from network.models import *

if not User.objects.count() > 1:
    user = get_user_model().objects.create_user('michael@gmail.com', 'test') # rushee
    user.firstName = 'Michael'
    user.lastName = 'Assefa'
    user.save()
    print 'Initialized user: %s' % str(user)

    user2 = get_user_model().objects.create_user('bill@gmail.com', 'test') # rushChair
    user2.firstName = 'Bill'
    user2.lastName = 'Koski'
    user2.save()
    print 'Initialized user: %s' % str(user2)

    user3 = get_user_model().objects.create_user('luis@gmail.com', 'test') # rushee
    user3.firstName = 'Luis'
    user3.lastName = 'Naranjo'
    user3.save()
    print 'Initialized user: %s' % str(user3)
else:
    user = User.objects.get(pk=1)
    user3 = User.objects.get(pk=3)

if not Recruit.objects.count() > 0:
    recruit = Recruit() # rushee contact info
    recruit.user = user
    recruit.grade = 'Freshman'
    recruit.phone = '206-787-2713'
    recruit.major = 'Electrical Engineering'
    recruit.bio = 'Loves to take long walks on the beach'
    recruit.save()
    print 'Intialized user (%s) as a rushee' % user

    recruit2 = Recruit()
    recruit2.user = user3
    recruit2.grade = 'Sophomore'
    recruit2.phone = '206-478-4652'
    recruit2.major = 'Undecided'
    recruit2.bio = 'I\m kind of on the fence about rushing'
    recruit2.save()
    print 'Intialized user (%s) as a rushee' % user3
else:
    recruit = Recruit.objects.get(pk=1)

if not Chapter.objects.count() > 0: # chapter rushee is rushing + chapter of rush chair
    chapter = Chapter()
    chapter.college = 'uw'
    chapter.name = 'Phi Delta Theta'
    chapter.save()
    recruit.subscribe(chapter)
    recruit2.subscribe(chapter)
    print 'Initialized chapter: %s' % chapter
    print 'Subscribed recruit (%s) to rush %s' % (recruit, chapter)
    print 'Subscribed recruit (%s) to rush %s' % (recruit2, chapter)
else:
    chapter = Chapter.objects.get(pk=1)
    

if not RushChair.objects.count() > 0:
    rushChair = RushChair() # rushChair deets
    rushChair.chapter = chapter
    rushChair.user = user2
    rushChair.save()
    print 'Intialized user (%s) as a rush chair' % user2
else:
    rushChair = RushChair.objects.get(pk=1)

fraternities = '''Delta Chi
Beta Theta Pi
Sigma Alpha Epsilon
Sigma Phi Epsilon
Zeta Beta Tau
Phi Psi
Pi Kappa Alpha
Alpha Delta Phi
Alpha Epsilon Pi
Alpha Sigma Phi
Alpha Tau Omega
Chi Psi
Delta Tau Delta
Delta Upsilon
Kappa Alpha Order
Kappa Sigma
Phi Gamma Delta
Pi Kappa Phi
Phi Kappa Psi
Phi Kappa Tau
Phi Kappa Theta
Sigma Beta Rho
Sigma Nu
Tau Kappa Epsilon
Theta Chi
Theta Delta Chi
Zeta Psi
Lambda Chi Alpha
Psi Upsilon'''

fraternities = fraternities.split('\n')
for name in fraternities:
    chapter, created = Chapter.objects.get_or_create(name=name, college='University of Washington')
    if created:
        print 'Initialized: %s' % chapter.name

