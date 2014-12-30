from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.views.generic import TemplateView

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'home.views.index', name='home'),
    url(r'^chapters/', include('chapters.urls', namespace='chapters')),
    url(r'^grades/', include('ifc_grades.urls', namespace='grades')),
    url(r'^admin/', include(admin.site.urls)),
)
