from django.conf.urls import url
from django.contrib.auth.views import logout
from . import views


urlpatterns = [
	url(r'^registro/$', views.Registration.as_view(),name="registro"),
	url(r'^profile/$', views.Dashboard.as_view(), name="profile"),
	url(r'^login/$', 'django.contrib.auth.views.login', name="login"),
	url(r'^logout/$', logout, name="logout"),
	url(r'^logout-then-login/$', 'django.contrib.auth.views.logout_then_login', name="logout_then_login"),
]