from django.shortcuts import render
from django.views.generic import ListView

from chapters.models import Chapter

class ChapterListView(ListView):
    model = Chapter
    template_name = 'chapters/index.html'
    context_object_name = 'chapters'
