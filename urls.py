from django.conf.urls.defaults import *
from django.views.generic.simple import redirect_to

from django_messages.views import *

urlpatterns = patterns('',
    url(r'^$', redirect_to, {'url': 'inbox/'}),
    url(r'^inbox/$', inbox, name='messages_inbox'),
    url(r'^outbox/$', outbox, name='messages_outbox'),
            )
