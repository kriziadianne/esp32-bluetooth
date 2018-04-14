from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic import TemplateView
from . import views

urlpatterns = [
 #    url(r'^admin/', admin.site.urls),
	# ## random name, views.function name, random name ##
 #    url(r'^contactlive', views.contactFormSucc, name="contactsucc"),
 #    url(r'^login', views.SignInForm, name='login'), ## changed to login form
 #    url(r'^SignIn', views.SignIn, name='signin'), ## doctor login
 #    url(r'registerform', views.signupForm, name = 'signup'), ## registration form
 #    url(r'signuppost', views.signuppost), ## doctor registration
 #    url(r'^$', views.home, name = "home"),
 #    url(r'^home', views.home_log, name = "home_log"), ## wala naman unta ni
 #    url(r'^logout', views.logout, name='log'),
 #    url(r'^dashboard/$', views.dashboard, name='dash'), ## doctor dashboard
 #    url(r'^pform', views.createform, name='pform'), ## add patient form
 #    url(r'^psucc', views.createpat, name='padd'), ## add patient
 #    url(r'^v2frm', views.impCredentials, name='impCred'),
 #    url(r'^v2rify', views.impForm, name ='impForm'),

 #    url(r'^patientdash/$', views.patientdash, name='pdash'), ## patient dashboard
 #    url(r'^docprof/update', views.updoc, name='updoc'), ## update doctor form
 #    url(r'^updatedprof', views.updatedprof, name='updatedprof'), ## updated doctor profile
 #    url(r'^patientprof/update', views.uppat, name='uppat'), ## update patient
 #    url(r'^updatedpatprof', views.updatedpatprof, name='updatedpatprof'), ## updated patientprofile
 #    url(r'chart', views.chart, name='chart'), ## bp chart
 #    url(r'^notif', views.notif, name='notif'),
 #    url(r'^vform', views.inputCredentialsForm, name="inpFCred"),
 #    url(r'^verify', views.inputCredentials, name="inpCred"),
 #    url(r'^contact', views.contactForm, name="contact"),

     url(r'^admin/', admin.site.urls),
    ## random name, views.function name, random name ##
    url(r'^contactlive', views.ContactPatient, name="contactsucc"),
    url(r'^login', views.LoginForm, name='login'), ## changed to login form
    url(r'^logging-in', views.Login, name='signin'), ## doctor login
    url(r'register', views.RegistrationForm, name = 'signup'), ## registration form
    url(r'registering', views.Register), ## doctor registration
    url(r'^$', views.home, name = "home"),
    url(r'^home', views.home_log, name = "home_log"), ## wala naman unta ni
    url(r'^logout', views.Logout, name='log'),
    url(r'^doctor-dashboard/$', views.DoctorDashboard, name='dash'), ## doctor dashboard
    url(r'^add-patient', views.AddPatientForm, name='pform'), ## add patient form
    url(r'^success-add-patient', views.AddPatient, name='padd'), ## add patient
    url(r'^add-patient/verify', views.impCredentials, name='impCred'),   ## add patient verify credentials
    url(r'^verifying', views.impForm, name ='impForm'),    ## add patient verify credentials form
    url(r'^patient-dashboard/$', views.PatientDashboard, name='pdash'), ## patient dashboard
    url(r'^doctor-profile/Update', views.UpdateDoctorProfile, name='updoc'), ## update doctor form
    url(r'^updatedprof', views.UpdatedDoctorProfile, name='updatedprof'), ## updated doctor profile
    url(r'^patient-profile/update', views.UpdatePatientProfile, name='uppat'), ## update patient
    url(r'^updatedpatprof', views.UpdatePatientProfile, name='updatedpatprof'), ## updated patientprofile
    url(r'BPchart', views.Chart, name='chart'), ## bp chart
    url(r'^notif', views.notif, name='notif'),
    url(r'^view-patient-list/verify', views.ViewPatientVerifyCredentialsForm, name="inpFCred"),
    url(r'^verifying', views.PatientListVerifyCredentials, name="inpCred"),
    url(r'^contact-patient', views.ContactPatientForm, name="contact"),
]
