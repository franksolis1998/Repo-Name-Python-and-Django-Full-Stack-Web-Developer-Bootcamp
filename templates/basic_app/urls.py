from django.conf.urls import path
from advance_section.basic_app.views import SchoolCreateView
from basic_app import views

app_name = 'basic_app'

urlpatterns = [
    path('',views.SchoolListView.as_view(),name='list')
    path('(?P<pk>[-\w +)/$', views.SchoolDetailView.as_view(),name='detail')
    path('create/$',views.SchoolCreateView.as_view(),name='create')
    path('update/(?P<pk>\d+)/$', views.SchoolUpdateView.as_view(),name='update'),
    path('delete/(?P<pk>[-\w +)/$', views.SchoolDeletelView.as_view(),name='delete')
]
