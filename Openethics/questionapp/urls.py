from django.conf.urls import *
from django.views.generic.simple import direct_to_template


urlpatterns = patterns('questionapp.views',
        
          url(r'^qs/(?P<questionnaire_id>\d+)/(?P<order_info>\d+)/$', 
          view = 'get_next_questiongroup',
          name = 'get_next_questiongroup'),
        
          url(r'^qs/(?P<questionnaire_id>\d+)/$', 
          view = 'get_next_questiongroup',
          name = 'get_next_questiongroup'),
                       
        url(r'^finish/$', 
            view = 'finish',
            name = 'questionnaire_finish'),                  
    
    
)

