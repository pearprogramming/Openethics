from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template


urlpatterns = patterns('',
      (r'^$', direct_to_template,
       
       
          { 'template': 'answer_form.html' }, 'index'),
                       
                       )