from django.views.generic import TemplateView
from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from .models import User
#from .forms import AddAlumniForm
from django.contrib.auth import login, authenticate
from django.urls import reverse
from django.views.generic.list import ListView
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views.generic import View,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from .filters import AlumniFilter
from django.urls import reverse_lazy


def home(request):
    return render(request,'home.html')

def AlumniListView(request):
    total = User.objects.all()
    alfilter = AlumniFilter(request.GET, queryset=total)
    template_name = 'showalumni.html'        
    return render(request,template_name,{'filter':alfilter})    

class AlumniDetailView(View):
    def get(self,request,*args, **kwargs):
        alumni = get_object_or_404(User,pk=kwargs['pk'])
        context = {'alumni':alumni}
        return render(request,"alumni.html",context)        