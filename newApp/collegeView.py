from django.shortcuts import redirect, render
from django.views.generic import CreateView, ListView
from .models import User
from .forms import CollegeSignupForm
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import UpdateView
from django.urls import reverse


def profile(request):
    return render(request, 'newApp/college/profile.html')


class SignupView(CreateView):
    model = User
    form_class = CollegeSignupForm
    template_name = 'registration/signup_form.html'

    def get_context_data(self, **kwargs):
        kwargs['user_type'] = 'college'
        return super().get_context_data(**kwargs)

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('home')


class PendingQueryView(ListView):
    def get_queryset(self):
        return User.objects.filter(
            Verified=False,
            is_alumni=True,
            College=self.request.user.username)
    template_name = "pendingalumni.html"
    context_object_name = 'alumnis'
    ordering = ['Year_Joined']
    paginate_by = 12


class AlumniAuthenticationView(LoginRequiredMixin, UpdateView):
    model = User
    fields = [
        "username",
        "first_name",
        "last_name",
        "email",
        "College",
        "About",
        "Work",
        "Year_Joined",
        "Branch",
        "Image",
        "Verified"
        ]
    template_name = 'verify.html'

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('pending-query')
