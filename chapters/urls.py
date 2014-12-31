from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from chapters import views

urlpatterns = patterns('',
    url(r'^$', views.ChapterListView.as_view(), name='index'),
    url(r'(?P<chapter>\w+)/$', views.ChapterDetailView.as_view(), name='profile'),
)
