from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from .models import AlumniDetailModel


class AddAlumniForm(forms.ModelForm):
    class Meta:
        model = AlumniDetailModel
        fields="__all__"