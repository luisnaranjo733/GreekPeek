from django.conf import settings
from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django_facebook.models import FacebookModel, get_user_model
from django_facebook.utils import get_profile_model
from django.contrib.auth.models import AbstractUser, UserManager

from network.choices import states


class Campus(models.Model):
    name = models.CharField(max_length=255)
    nickname = models.CharField(max_length=80, blank=True, null=True, unique=True)
    state = models.CharField(max_length=80, choices=states)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return '/campus/%s/' % self.__str__()

class CustomFacebookUser(AbstractUser, FacebookModel):
    '''
    The django 1.5 approach to adding the facebook related fields
    '''
    objects = UserManager()
    # add any customizations you like
    campus = models.ForeignKey(Campus, blank=True, null=True, on_delete=models.SET_NULL) # prevent cascading


