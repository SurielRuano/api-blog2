from django.conf.urls import url
from  . import  views


urlpatterns = [
	
	url(r'^posts/$',
		views.PostListView.as_view(),
		name='posts_lists'),

	url(r'^posts/(?P<pk>\d+/)$',
		views.PostDetailView.as_view(),
		name = 'post_detail'),
	
]