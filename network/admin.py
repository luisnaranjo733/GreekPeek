from django.contrib import admin

# Register your models here.
from network.models import CustomFacebookUser, Campus

admin.site.register(CustomFacebookUser)
admin.site.register(Campus)
