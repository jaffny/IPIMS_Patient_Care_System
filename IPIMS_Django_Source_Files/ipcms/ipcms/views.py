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
from .forms import PatientApptForm
from django.template import RequestContext
from django.shortcuts import render

STAFF_APPROVAL_ROLES = ('admin', 'doctor', 'staff', 'nurse', 'lab')

'''
Homepage to display the main control panel or HomePage based on user authentication
'''

class HomePageView(generic.TemplateView):
	template_name = 'home.html'
	def get(self, request):

		#Model Definitions & Declarations
		permissionModel = PermissionsRole
		patientModel = Patient

		#Assign default permission role
		permissionRoleForUser = 'pending'

		#Assign a default approval rating
		approval = 0

		#Assign a default authentication boolean
		authenticated = False

		#Check to see if the user has logged into the system or not
		if request.user.is_authenticated():

			#Boolean to ensure valid request authentication
			authenticated = True

			#Attempt a DB query on the request object
			if permissionModel.objects.filter(user__username=request.user.username)[:1].exists():

				#If request object from query exists, create a variable assignment on that object
				permissionRoleForUser = permissionModel.objects.filter(user__username=request.user.username)[:1].get()

				#If the logged in person is a patient, grab request object, make a query and grab the approval integer
				if patientModel.objects.filter(user__username=request.user.username)[:1].exists():

					#Get an integer declaraction for the approval of the user
					approvalSwitch = patientModel.objects.filter(user__username=request.user.username)[:1].get()

				#If the person is a hospital member, then they will automatically be considered approved
				if (permissionRoleForUser.role in STAFF_APPROVAL_ROLES):
					approval = 1
				else:
					approval = approvalSwitch.approved

		#Under the instance that the user is not authenticated
		else:
			permissionRoleForUser = ""

		return render_to_response('accounts/controlpanel.html', {'permissionModel': permissionModel, 'user': request.user, 'roles': permissionRoleForUser, 'approval': approval, 'authenticated': authenticated})

'''
Basic success page response rendering for the user
'''

class SuccessPageView(generic.TemplateView):
	template_name = 'accounts/success.html'

'''
Sign up view used to register a user into the system
'''

class SignUpView(generic.CreateView):

	form_class = RegistrationForm
	model = User 
	template_name = 'accounts/signup.html'
	success_url = reverse_lazy('Success')


'''
Login view for the user to redirect into the patient/admin portal
'''

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

'''
View that is responsible for rendering the patient scheduling system for the user
'''

def ScheduleView(request):

	title = "Appointment Schedule"
	form = PatientApptForm(request.POST or None)

	patient_model = Patient
	if form.is_valid():
		instance = form.save(commit=False)
		patient = patient_model.objects.filter(user__username=request.user.username)[:1].get()
		instance.patient = patient
		instance.user = patient
		instance.save()
		return HttpResponseRedirect('success/')
	context = {
		"form": form,
		"template_title": title
	}
	return render(request, 'accounts/schedule.html', context)

'''
View that forces request object to log out of the system
'''

def logout_user(request):
	logout(request)
	return HttpResponseRedirect(reverse_lazy('Home'))


class CreatePatientView(generic.CreateView):
	model = Patient
	template_name = 'accounts/controlpanel.html'
	form_class = PatientForm
	success_url = reverse_lazy("FormTest")



