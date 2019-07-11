
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from django.conf import settings
from django.views.static import serve
from loginap import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$',views.home),
	url(r'^register/',views.register),
	url(r'^login/',views.login),
	url(r'^Enquiryview/',views.Enquiryview),
	url(r'^admin2/',views.admin2),
	url(r'^jobs/',views.jobs),
	url(r'^author/',views.author),
	url(r'^newsletter/',views.newsletter),
	url(r'^newsletter2/',views.newsletter2)

]
if settings.DEBUG:
    urlpatterns +=[
        url(r'^media/(?P<path>.*)$',serve,{
            'document_root':settings.MEDIA_ROOT,
        }),
    ]

