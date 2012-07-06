from django.conf.urls import *
from django.views.generic.simple import direct_to_template
from questionapp.views import *

urlpatterns = patterns('questionapp.views',
        
        url(r'^first/$', 
            view = 'first_questionset',
            name = 'first_questionset'),
#       url(r'^questionnaire/(?P<questionnaire_id>\d+)/$',view='questionnaire_questions',name='questionnaire_questions') ,
        url(r'^questionnaire/(?P<questionnaire_id>\d+)/$',view='questionnaire_questions1',name='questionnaire_questions1') ,           
        
        url(r'^success/$', 
            view = 'success_view',
            name = 'questionapp_success'),               
    
)

