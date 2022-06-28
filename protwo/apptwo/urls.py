from importlib.resources import path
from django.contrib import admin
from apptwo import views
from django.conf.urls import include

urlpatterns = [
    path('', views.index, name='help'),
    path('help/',include('apptwo.urls')),
    path('admin/',admin.site.urls),
]