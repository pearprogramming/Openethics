from django.conf.urls import *
from django.views.generic.simple import direct_to_template
from questionapp.views import *

urlpatterns = patterns('questionapp.views',
        
        url(r'^first/$', 
            view = 'first_questionset',
            name = 'first_questionset'),
        
        url(r'^success/$', 
            view = 'success_view',
            name = 'questionapp_success'),               
        
      #  url(r'^get/(?P<order_info>\d+)$', 
       #     view = 'get_next_questionsgroupid',
         #   name = 'get_next_questionsgroupid'),               
    
    
)

