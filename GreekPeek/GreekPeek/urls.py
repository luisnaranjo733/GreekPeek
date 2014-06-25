from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'network.views.home'),
    url(r'^signUp/', 'network.views.signUp'),
    url(r'^signIn/', 'network.views.logIn'),
    url(r'^fraternities/', 'network.views.fraternities'),
    url(r'^whyJoin/', 'network.views.whyJoin'),
    url(r'^rushAdmin/', 'network.views.rushAdmin'),
    url(r'^login/', 'network.views.logIn'),
    url(r'^logout/', 'network.views.logOut'),
    url(r'^contactUs/', 'network.views.contactUs'),
    url(r'^formComplete/', 'network.views.formComplete'),
    url(r'^policies/', 'network.views.policies'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^json/(.+)/$', 'network.views.ajax'),
    url(r'^names/', 'network.views.namesTest'),
    url(r'^profileSettings', 'network.views.profileSettings'),
    url(r'^profileSettings2', 'network.views.profileSettings2'),

)

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.STATIC_URL, document_root=settings.TEMPLATE_DIRS[0])
