'''
Created on Jun 26, 2012

@author: ayoola_al
'''
from django.contrib import admin
from questionapp.models import *
 
class QuestionAdmin(admin.ModelAdmin):
    list_display=('label','field_type','optionanswer')
    
class OptionAnswerAdmin(admin.ModelAdmin):
     
    list_display=('option',)  
    
class AnswerSetAdmin(admin.ModelAdmin):
    list_display=('user','question','answer')



class QuestiongroupAdmin(admin.ModelAdmin):
    list_display=('questiongroupname',)
    


class QuestionnaireInline(admin.TabularInline):
    model = Questionnaire.questiongroup.through
    
class QuestionnaireAdmin(admin.ModelAdmin):
    inlines = [
               QuestionnaireInline,
               ]
    exclude = ('questiongroup',)
    
class QuestionOrderAdmin(admin.ModelAdmin):
    list_display = ('questiongroup','questionnaire','order_info')
    
admin.site.register(OptionAnswer,OptionAnswerAdmin)
admin.site.register(Question,QuestionAdmin)
admin.site.register(AnswerSet,AnswerSetAdmin)
admin.site.register(Questiongroup,QuestiongroupAdmin)
admin.site.register(Questionnaire,QuestionnaireAdmin)
admin.site.register(QuestionOrder,QuestionOrderAdmin)