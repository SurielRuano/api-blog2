from django.conf.urls import url, include
from django.contrib import admin
from posts import urls as postUrls
from django.conf import settings
from accounts import urls as accUrls


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^blog/',include(postUrls,namespace="posts")),
    url(r'^accounts/', include(accUrls)),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(
        regex=r'^media/(?P<path>.*)$',
        view='django.views.static.serve',
        kwargs={'document_root':settings.MEDIA_ROOT}),
]
