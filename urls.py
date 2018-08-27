from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^logfiles/$', logfiles_list, name='logfiles_list'),
    url(r'^logfiles/(?P<logfile_id>\d+)$', logfile_view, name='logfile_view'),
]
