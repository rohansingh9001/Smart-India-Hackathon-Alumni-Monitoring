from django.contrib import admin
from django.urls import path
from django.conf.urls import include,url

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('main.urls')),
 	url(r'^accounts/', include('allauth.urls')),
]
