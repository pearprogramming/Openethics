'''
Created on 20 Jun 2012

@author: mzd2
'''
from django.contrib import admin
from Question.models import *

class EvaluationSchemeAdmin(admin.ModelAdmin):
    list_display = ('title',)

class EvaluationAdmin(admin.ModelAdmin):
    list_display = ('doctor', 'agency','scheme')

class EvaluationQuestionAdmin(admin.ModelAdmin):
    list_display = ('question', 'evaluation')

class EvaluationAnswerAdmin(admin.ModelAdmin):
    list_display = ('evaluation', 'question','answer')
    


    
admin.site.register(EvaluationScheme, EvaluationSchemeAdmin)
admin.site.register(Evaluation, EvaluationAdmin)
admin.site.register(EvaluationQuestion, EvaluationQuestionAdmin)
admin.site.register(EvaluationAnswer, EvaluationAnswerAdmin)