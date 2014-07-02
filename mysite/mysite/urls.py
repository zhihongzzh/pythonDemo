from django.conf.urls import patterns, include, url

from django.contrib import admin
from polls import views
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
	url(r'^polls/',include('polls.urls')),
	url(r'^polls/lastest\.html$','polls.views.index'),
)
