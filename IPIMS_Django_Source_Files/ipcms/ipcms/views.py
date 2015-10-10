from __future__ import absolute_import
from django.views import generic
from django.template import loader, Context
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse_lazy
from .forms import RegistrationForm, LoginForm, PatientForm
from django.template import RequestContext
from django.views.generic import ListView
from .models import PermissionsRole, Patient
from django.shortcuts import render_to_response




class HomePageView(generic.TemplateView):
	template_name = 'home.html'

class SignUpView(generic.CreateView):
	form_class = RegistrationForm
	model = User 
	template_name = 'accounts/signup.html'
	success_url = reverse_lazy('Home')


class LoginView(generic.FormView):
	form_class = LoginForm
	success_url = reverse_lazy('Home')
	template_name = 'accounts/login.html'

	def form_valid(self, form):
		username = form.cleaned_data['email']
		password = form.cleaned_data['password']
		user = authenticate(email=email, password=password)

		if user is not None and user.is_active:
			login(self.request, user)
			return super(LoginView, self).form_valid(form)
		else:
			return self.invalid(form)

#View that is related to show teh form to display the schedule appt for the user
class ScheduleView(generic.TemplateView):
	#Return the current permissions of the authenticated user
	def get(self, request):
		permissionModel = PermissionsRole
		context_object_name = 'permissionModel'

		if request.user.is_authenticated():
			permissionRoleForUser = permissionModel.objects.filter(user__username=request.user.username)[:1].get()

		else:
			HttpResponse("fail")
		return render_to_response('accounts/controlpanel.html', {'permissionModel': permissionModel, 'user': request.user, 'roles': permissionRoleForUser.role})

def logout_user(request):
	logout(request)
	return HttpResponseRedirect(reverse_lazy('Home'))


class CreatePatientView(generic.CreateView):

	model = Patient
	template_name = 'accounts/controlpanel.html'

	form_class = PatientForm
	success_url = reverse_lazy("FormTest")



