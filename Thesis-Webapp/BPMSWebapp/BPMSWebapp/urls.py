from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from BPMSWebapp.models import DocReg
from . import views

urlpatterns = [

    url(r'^admin/', admin.site.urls),
    ## random name, views.function name, random name ##
    url(r'^contactlive', views.ContactPatient, name="contactsucc"),
    url(r'^login', views.LoginForm, name='login'), ## changed to login form
    url(r'^SignIn', views.Login, name='signin'), ## doctor login
    url(r'registerform', views.RegistrationForm, name = 'signup'), ## registration form
    url(r'signuppost', views.Register, name = 'signuppost'), ## doctor registration
    #     url(r'signuppost', views.Register.as_view(queryset=request.POST.get())), ## doctor registration
    url(r'^$', views.home, name = "home"),
    url(r'^home', views.home_log, name = "home_log"), ## wala naman unta ni
    url(r'^logout', views.Logout, name='log'),
    url(r'^dashboard/$', views.DoctorDashboard, name='dash'), ## doctor dashboard
    url(r'^pform', views.AddPatientForm, name='pform'), ## add patient form
    url(r'^psucc', views.AddPatient, name='padd'), ## add patient
    url(r'^v2frm', views.impCredentials, name='impCred'),
    url(r'^v2rify', views.impForm, name ='impForm'),

    url(r'^patientdash/$', views.PatientDashboard, name='pdash'), ## patient dashboard
    url(r'^docprof/update', views.UpdateDoctorProfile, name='updoc'), ## update doctor form
    url(r'^updatedprof', views.UpdatedDoctorProfile, name='updatedprof'), ## updated doctor profile
    url(r'^patientprof/update', views.UpdatePatientProfile, name='uppat'), ## update patient
    url(r'^updatedpatprof', views.UpdatePatientProfile, name='updatedpatprof'), ## updated patientprofile
    url(r'chart', views.Chart, name='chart'), ## bp chart
    url(r'^notif', views.notif, name='notif'),
    url(r'^vform', views.ViewPatientVerifyCredentialsForm, name="inpFCred"),
    url(r'^verify', views.PatientListVerifyCredentials, name="inpCred"),
    url(r'^contact', views.ContactPatientForm, name="contact"),
]
