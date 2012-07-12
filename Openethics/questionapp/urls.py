from django.conf.urls import *
from django.views.generic.simple import direct_to_template
from questionapp.views import *

urlpatterns = patterns('questionapp.views',
        
          url(r'^quest/(?P<questionnaire_id>\d+)/(?P<order_info>\d+)/$', 
          view = 'get_next_questiongroup',
          name = 'get_next_questiongroup'),
        
          url(r'^quest/(?P<questionnaire_id>\d+)/$', 
          view = 'get_next_questiongroup',
          name = 'get_next_questiongroup'),
                       
        url(r'^finish/$', 
            view = 'finish',
            name = 'questionaire_finish'),                  
    
    
)

