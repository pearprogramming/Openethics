from django.conf.urls import patterns, url


urlpatterns = patterns('ethicsapplication.views',
      url(r'^create$',
          view ='create_application', 
          name='create_application_view'), #creation view
)