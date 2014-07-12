from django.db import models
from django_facebook.models import FacebookModel
from django.contrib.auth.models import AbstractUser, UserManager

class CustomFacebookUser(AbstractUser, FacebookModel):
    '''
    The django 1.5 approach to adding the facebook related fields
    '''
    objects = UserManager()
    # add any customizations you like
    state = models.CharField(max_length=255, blank=True, null=True)


