from __future__ import absolute_import
from django.views import generic
from django.template import loader, Context
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate, login, logout
from django.core.urlresolvers import reverse_lazy
from .forms import RegistrationForm, LoginForm



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
		username = form.cleaned_data['username']
		password = form.cleaned_data['password']
		user = authenticate(username=username, password=password)

		if user is not None and user.is_active:
			login(self.request, user)
			return super(LoginView, self).form_valid(form)
		else:
			return self.invalid(form)

def logout_user(request):
	logout(request)
	return HttpResponseRedirect(reverse_lazy('Home'))