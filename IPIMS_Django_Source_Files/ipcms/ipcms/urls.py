"""ipcms URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', HomePageView, name='Home'),
    url(r'formsuccess/$', SuccessFormPageView.as_view(), name="DataSubmitted"),
    url(r'success/$', SuccessPageView.as_view(), name='Success'),
    url(r'accounts/apply/$', SignUpView.as_view(), name="Signup"),
    url(r'accounts/login/$', LoginView.as_view(), name="Login"),
    url(r'^accounts/portal/$', PatientPortalView, name="Portal"),
    url(r'logout/$', logout_user, name="Logout"),
    url(r'^super/', include(admin.site.urls)),
    url(r'^schedule/$', ScheduleView, name="Schedule"),
    url(r'^health_conditions/$', HealthConditionsView, name="Conditions"),
    url(r'^search/$', PatientSearch, name="PatientSearch"),
    url(r'^delete/$', DeleteUser, name="DeleteUser"),
    url(r'^alert/$', AlertSender, name="Alert"),
    url(r'^accounts/portal/view_alerts/$', EmergencyAlerts, name="ViewAlerts"),
    url(r'^accounts/portal/update_account/$', UpdateAccountView, name="Update"),
    url(r'^accounts/portal/view_appts/$', ApptView, name="ViewAppts"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

