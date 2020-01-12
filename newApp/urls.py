from django.urls import include, path
from . import views,alumniView,collegeView
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import url

urlpatterns = [
	path('',views.home,name='home'),
    path('/alumni',alumniView.profile,name="alumni-profile"),
    path('showalumni',views.AlumniListView,name="show-alumni"),
    path('alumni/<int:pk>/', views.AlumniDetailView.as_view(),name="alumni-detail"),
    path('college/query/',collegeView.PendingQueryView.as_view(),name="pending-query"),
    path('authenticate/<int:pk>/', collegeView.AlumniAuthenticationView.as_view(),name="alumni-authentication"),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)