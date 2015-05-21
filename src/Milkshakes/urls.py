from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	url(r'^admin/', include(admin.site.urls)),
    url(r'^$', 'joinmech.views.home', name='home'),

    #allows us to accept reference ID into url by using an argument
    url(r'^(?P<ref_id>.*)$', 'joinmech.views.share', name=''),
)
