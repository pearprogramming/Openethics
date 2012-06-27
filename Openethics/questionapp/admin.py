'''
Created on 26 Jun 2012

@author: ala23
'''
from django.contrib import admin
from questionapp.models import *

class SchemeAdmin(admin.ModelAdmin):
    list_display = ('name','scheme_date')
class QuestionAdmin(admin.ModelAdmin):
    list_display =('scheme','label', 'field_type')
    
    
admin.site.register(Scheme,SchemeAdmin)
admin.site.register(Question,QuestionAdmin)

    
    