from django.contrib import admin

# Register your models here.
from network.models import CustomFacebookUser

admin.site.register(CustomFacebookUser)
