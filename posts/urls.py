from django.conf.urls import url
from . import views

urlpatterns = [
url(r'^nuevo/$', views.FormView.as_view(),name="nuevo"),
url(r'^(?P<slug>[-\w]+)/$', views.DetailView.as_view(), name="detalle"),
url(r'^$', views.ListView.as_view(), name="lista"),
]