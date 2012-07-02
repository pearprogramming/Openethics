'''
Created on Jun 26, 2012

@author: ayoola_al
'''
from django.contrib import admin
from questionapp.models import *
 
class QuestionAdmin(admin.ModelAdmin):
    list_display=('questiongroup','label','field_type')
    
class QuestiongroupAdmin(admin.ModelAdmin):
    list_display=('questiongroupname','order_no')
    
class AnswerSetAdmin(admin.ModelAdmin):
    list_display=('user','question','answer')

admin.site.register(Question,QuestionAdmin)
admin.site.register(AnswerSet,AnswerSetAdmin)
admin.site.register(Questiongroup,QuestiongroupAdmin)
