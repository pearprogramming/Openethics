'''
Created on 20 Jun 2012

@author: mzd2
'''
from django.contrib import admin
from Question.models import *





class PrescreenQuestionAdmin(admin.ModelAdmin):
    list_display = ('PreQuestion','PreQuestionFlag')



class QuestionSetAdmin(admin.ModelAdmin):
    list_display = ('title',)

class UserAdmin(admin.ModelAdmin):
    list_display = ('User', 'Type','Set')

class QuestionBankAdmin(admin.ModelAdmin):
    list_display = ('question', 'QSet')

class EvaluationAnswerAdmin(admin.ModelAdmin):
    list_display = ('evaluation', 'question','answer')
    


admin.site.register(PrescreenQuestion, PrescreenQuestionAdmin)    
admin.site.register(QuestionSet, QuestionSetAdmin)
admin.site.register(User, UserAdmin)
admin.site.register(QuestionBank, QuestionBankAdmin)
admin.site.register(EvaluationAnswer, EvaluationAnswerAdmin)