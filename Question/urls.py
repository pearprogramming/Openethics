from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template


urlpatterns = patterns('Question.views',
                       
   url(r'^(?P<id>\d+)/$',
     'answer_form',
   
    ),                        

   # url(r'^(?P<id>\d+)/$',
   #  view='prepare_blank_answers',
   
   # ),                       

)

