from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.shortcuts import get_object_or_404


from chapters.models import Chapter

class ChapterListView(ListView):
    model = Chapter
    template_name = 'chapters/index.html'
    context_object_name = 'chapters'
    
class ChapterDetailView(DetailView):
    model = Chapter
    template_name = 'chapters/profile.html'
 
    def get_object(self):
        return get_object_or_404(Chapter, name=request.session['chapter'])
