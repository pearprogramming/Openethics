'''
Created on Jun 26, 2012

@author: ayoola_al

'''
from django.forms import forms
from models import *

FIELD_TYPES={
            0: forms.CharField(max_length=100),
            1: forms.CharField(widget = forms.Textarea),
            2: forms.BooleanField(initial= False)
            }
def make_question_scheme_form(scheme_id):
    '''
     mapping questions field to type form fields @return: form for specific scheme  
    
    '''
    scheme = Scheme.objects.get(scheme_id).questions.all()
    
    fields={}
    #for question in scheme.questions.all():
    for question in scheme:
        fields[question.label]= FIELD_TYPES[question.field_type](label=question.label)
    return type('SchemeForm',(forms.BaseForm,),{'base_fields':fields})
