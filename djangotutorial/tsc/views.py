from django.views import generic
from django.utils import timezone

from .models import Scene

# Create your views here.
class IndexView(generic.ListView):
    template_name = "tsc/index.html"
    context_object_name = "scene_list"

    def get_queryset(self):
        return Scene.objects.all()



class DetailView(generic.DetailView):
    model = Scene
    template_name = "tsc/detail.html"
    
    def get_queryset(self):
        """
        Excludes any questions that aren't published yet.
        """
        return Scene.objects.all()