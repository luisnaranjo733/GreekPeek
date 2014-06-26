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

if not User.objects.count() > 2:
    user = get_user_model().objects.create_user('john@gmail.com', 'test')
    user.firstName = 'john'
    user.lastName = 'Dahl'
    user.save()

    user2 = get_user_model().objects.create_user('bill@gmail.com', 'test')
    user2.firstName = 'bill'
    user2.save()
else:
    user = User.objects.get(pk=1)

if not Recruit.objects.count() > 0:
    recruit = Recruit()
    recruit.user = user
    recruit.grade = 'Freshman'
    recruit.phone = '206-478-4652'
    recruit.major = 'bioE'
    recruit.bio = 'Loves to take long walks on the beach'
    recruit.save()
else:
    recruit = Recruit.objects.get(pk=1)

if not Chapter.objects.count() > 0:
    chapter = Chapter()
    chapter.college = 'uw'
    chapter.name = 'Phi Delta Theta'
    chapter.save()
else:
    chapter = Chapter.objects.get(pk=1)

if not RushChair.objects.count() > 0:
    rushChair = RushChair()
    rushChair.chapter = chapter
    rushChair.user = user2
    rushChair.save()
else:
    rushChair = RushChair.objects.get(pk=1)

fraternities = '''Delta Chi
Beta Theta Pi
Sigma Alpha Epsilon
Sigma Phi Epsilon
Zeta Beta Tau
Phi Psi
Pi Kappa Alpha
Alpha Delpha Phi
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
