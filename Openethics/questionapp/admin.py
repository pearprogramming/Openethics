'''
Created on Jun 26, 2012

@author: ayoola_al
'''
from django.contrib import admin
from questionapp.models import *
 
class QuestionAdmin(admin.ModelAdmin):
    list_display=('questiongroup','label','field_type')
    
class QuestiongroupAdmin(admin.ModelAdmin):
    list_display=('questiongroupname','date_created','order_no')
    
class QuestionAnswerAdmin(admin.ModelAdmin):
    list_display=('user','questiongroup','question','answer','status')

admin.site.register(Question,QuestionAdmin)
admin.site.register(QuestionAnswer,QuestionAnswerAdmin)
admin.site.register(Questiongroup,QuestiongroupAdmin)
