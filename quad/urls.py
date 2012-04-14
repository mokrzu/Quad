from django.conf.urls import patterns, include, url
from mongoengine import connect

# Start connection to mongo database
connect("quad_db")

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'quad.views.home', name='home'),
    # url(r'^quad/', include('quad.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    # Quad urls
    url(r'^$', 'app.views.home'),
    url(r'^new/$', 'app.views.new'),
    url(r'^create/$', 'app.views.create'),
    url(r'^(?P<question_id>\w+)/$', 'app.views.question'),
    url(r'^answer/(?P<question_id>\w+)$', 'app.views.answer'),
    url(r'^confirm/(?P<question_id>\w+)$', 'app.views.confirm'),
    url(r'^delete/(?P<question_id>\w+)$', 'app.views.delete'),
) 
