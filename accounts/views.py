from django.shortcuts import render
from django.views.generic import View

from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required

class Dashboard(View):
	@method_decorator(login_required)
	def get(self, request):
		template_name="accounts/perfil.html"
		context = {}
		return render(request,template_name,context)
