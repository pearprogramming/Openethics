'''
Created on Jun 26, 2012

@author: ayoola_al
'''
from django.contrib import admin
from questionapp.models import *
 
class QuestionAdmin(admin.ModelAdmin):
    list_display=('label','field_type')
    

    
class AnswerSetAdmin(admin.ModelAdmin):
    list_display=('user','question','answer')



class QuestiongroupAdmin(admin.ModelAdmin):
    list_display=('questiongroupname', 'question')
    

    


admin.site.register(Question,QuestionAdmin)
admin.site.register(AnswerSet,AnswerSetAdmin)
admin.site.register(Questiongroup,QuestiongroupAdmin)
