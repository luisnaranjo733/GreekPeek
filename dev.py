import os
import sys
from pprint import pprint
path = os.path.join('/home/lnaran/webapps/dev/GreekPeek', 'GreekPeek')
sys.path.append(path)
os.environ['DJANGO_SETTINGS_MODULE'] = 'GreekPeek.settings'

from django.contrib.auth import get_user_model

from network.models import *

User = get_user_model()
user = User.objects.get(pk=2)

def search(key, user):
    for attr in dir(user):
        if key in attr:
            print attr

for user in User.objects.all():
    print 'Full name: %s' % user.get_full_name()
    print 'Email: %s' % user.email
