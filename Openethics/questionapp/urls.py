from django.conf.urls import *
from django.views.generic.simple import direct_to_template
from questionapp.views import *

urlpatterns = patterns('questionapp.views',
        
        url(r'^first/(?P<questiongroup_id>\d+)$', 
            view = 'first_questionset',
            name = 'first_questionset'),
        
        url(r'^success/$', 
            view = 'success_view',
            name = 'questionapp_success'),               
        
        url(r'^get/(?P<order_info>\d+)/(?P<questionnaire>\d+)/$', 
            view = 'get_next_questionsgroupid',
            name = 'get_next_questionsgroupid'),
        
        url(r'^qs/(?P<questionnaire_id>\d+)$', 
            view = 'get_questionnaire',
            name = 'get_questionnaire'),                   
    
    
)

