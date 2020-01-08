from django.shortcuts import render,redirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from .models import AlumniDetailModel
from .forms import AddAlumniForm
from django.contrib.auth import login, authenticate
from django.urls import reverse
from django.views.generic.list import ListView
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.views.generic import View,UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

from django.urls import reverse_lazy
def home(request):
	return render(request,'home.html')

class AddAlumniView(CreateView):
    model = AlumniDetailModel
    fields = ['Name','College','Branch','About','Work','Year_Joined','Contact','Email','Image']
    template_name = 'addalumni.html'

    def form_valid(self, form):
        form.instance.Verified = False
        return super().form_valid(form)

class AlumniListView(ListView):
    queryset = AlumniDetailModel.objects.filter(Verified=True)
    template_name = 'showalumni.html'
    context_object_name = 'alumnis'
    ordering = ['Year_Joined']
    paginate_by = 12        

class AlumniDetailView(View):
    def get(self,request,*args, **kwargs):
        alumni = get_object_or_404(AlumniDetailModel,pk=kwargs['pk'])
        context = {'alumni':alumni}
        return render(request,"alumni.html",context)    

class PendingQueryView(ListView):
   def get_queryset(self):
        return AlumniDetailModel.objects.filter(Verified=False,College=self.request.user)    
   template_name = "pendingalumni.html"
   context_object_name = 'alumnis'
   ordering = ['Year_Joined']
   paginate_by = 12

class UserprojectList(ListView):
    context_object_name = 'userproject_list'
    template_name = 'userproject_list.html'
    def get_queryset(self):
        return Userproject.objects.filter(user=self.request.user)

class AlumniAuthenticationView(LoginRequiredMixin,UpdateView):
    model = AlumniDetailModel
    fields = ['Name','College','Branch','About','Work','Year_Joined','Contact','Email','Image','Verified']
    template_name = 'verify.html'

    def form_valid(self,form):
        return super().form_valid(form) 
    def get_success_url(self):
            return reverse('pending-query')        