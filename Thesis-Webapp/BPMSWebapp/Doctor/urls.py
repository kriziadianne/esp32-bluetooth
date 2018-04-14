from django.conf.urls import url
#from django.contrib.auth import views as auth_views
from . import views

app_name = 'Doctor'

urlpatterns = [

        url(r"dashboard/$", views.DashboardView.as_view(),name='dash'),

]
