from django.shortcuts import render
from django.shortcuts import get_object_or_404
from .models import User
# from .forms import AddAlumniForm
from django.views.generic import View
from .filters import AlumniFilter


def home(request):
    return render(request, 'home.html')


def AlumniListView(request):
    total = User.objects.all()
    alfilter = AlumniFilter(request.GET, queryset=total)
    template_name = 'showalumni.html'
    return render(request, template_name, {'filter': alfilter})


class AlumniDetailView(View):
    def get(self, request, *args, **kwargs):
        alumni = get_object_or_404(User, pk=kwargs['pk'])
        context = {'alumni': alumni}
        return render(request, "alumni.html", context)
