from django.shortcuts import render
from django.views.generic import View

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

from .forms import UserRegistrationForm

class Dashboard(View):
	@method_decorator(login_required)
	def get(self, request):
		template_name="accounts/perfil.html"
		context = {}
		return render(request,template_name,context)

class Registration(View):
	def get(self, request):
		template_name = "accounts/registration.html"
		form = UserRegistrationForm()
		context = {
		'form':form,
		}
		return render(request,template_name,context)

	def post(self,request):
		template_name = "accounts/registration.html"
		new_user_form = UserRegistrationForm(request.POST)
		if new_user_form.is_valid():
			new_user = new_user_form.save(commit=False)
			new_user.set_password(new_user_form.cleaned_data['password'])
			new_user.save()
			context = {}
			return render(request,template_name,context)
		else:
			context = {
			'form':new_user_form
			}
			return render(request,template_name,context)






