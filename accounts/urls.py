from django.conf.urls import url
from django.contrib.auth.views import logout
from . import views


urlpatterns = [
	url(r'^dashboard/$', views.Dashboard.as_view(), name="perfil"),
	url(r'^login/$', 'django.contrib.auth.views.login', name="login"),
	url(r'^logout/$', logout, name="logout"),
	url(r'^logout-then-login/$', 'django.contrib.auth.views.logout_then_login', name="logout_then_login"),
]