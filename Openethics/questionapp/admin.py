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

class AnswersAdmin(admin.ModelAdmin):
    list_display=('answerset')

class QuestiongroupAdmin(admin.ModelAdmin):
    list_display=('questiongroupname',)
    
class Questionnaire_QuestiongroupInline(admin.TabularInline):
    model = Questionnaire_Questiongroup
    extra = 1


class QuestionnaireInline(admin.TabularInline):
#    model = Questionnaire.questiongroups.through
    inlines=(Questionnaire_QuestiongroupInline,)
    
class QuestionnaireAdmin(admin.ModelAdmin):
    inlines = [
               Questionnaire_QuestiongroupInline,
               ]
#    exclude = ('questiongroup',)

    

admin.site.register(Question,QuestionAdmin)
admin.site.register(AnswerSet,AnswerSetAdmin)
admin.site.register(Questiongroup,QuestiongroupAdmin)
admin.site.register(Questionnaire,QuestionnaireAdmin)
#admin.site.register(Answers,AnswersAdmin)