from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
     url(r'^$', 'poll_app.views.home', name='home'),
     url(r'^login/$','poll_app.views.login_view', name='login'),
     url(r'^logout/$','poll_app.views.logout_view', name='logout'),
     url(r'^add_poll/$','poll_app.views.add_poll', name='add_poll'),
     url(r'^view_poll/(?P<poll_id>\d+)/$','poll_app.views.view_poll', name='view_poll'),
     url(r'^add_choice/(?P<poll_id>\d+)/$','poll_app.views.add_choice', name='add_choice'),
     url(r'^vote/$','poll_app.views.vote', name='vote'),
     url(r'^delete_poll/(?P<poll_id>\d+)/$','poll_app.views.delete_poll', name='delete_poll'),
    # url(r'^poll/', include('poll.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
)
