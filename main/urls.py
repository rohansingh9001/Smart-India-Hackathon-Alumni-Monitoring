from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django_filters.views import FilterView
from .filters import AlumniFilter

urlpatterns = [
    path('',views.home,name="home"),
    path('addalumni',views.AddAlumniView.as_view(success_url='/'),name="add-alumni"),
    path('showalumni',views.AlumniListView,name="show-alumni"),
    path('alumni/<int:pk>/', views.AlumniDetailView.as_view(),name="alumni-detail"),
    path('authenticate/<int:pk>/', views.AlumniAuthenticationView.as_view(),name="alumni-authentication"),
    path('college/query/',views.PendingQueryView.as_view(),name="pending-query")

]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
