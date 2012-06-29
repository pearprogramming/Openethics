from django.conf.urls import *
from django.views.generic.simple import direct_to_template
from questionapp.views import *

urlpatterns = patterns('questionapp.views',
        
        url(r'^first/(?P<questiongroup_id>\d+)/$', 'first_questionset'),
                       
    
)