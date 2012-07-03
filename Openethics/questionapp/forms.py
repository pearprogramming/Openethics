'''
Created on Jun 26, 2012

@author: ayoola_al

'''

from django import forms
from models import Questiongroup
from django.forms.fields import CharField,BooleanField



FIELD_TYPES={
            0: CharField(max_length=100) ,
            1: CharField(widget = forms.Textarea),
            2: BooleanField(initial= False)
            }
def make_question_group_form(questiongroup_id):
    '''
     mapping questions fields  type  to form fields type 
     @return: type form for specific questiongroup 
    
    '''
    fields={}
    thisgroupquestions = Questiongroup.objects.get(id=questiongroup_id).questions.all()
    
    
    
    #for question in scheme.questions.all():
    for question in thisgroupquestions:
        
        field = FIELD_TYPES[question.field_type] 
        field.label = question.label
        fields[str(question.id)]= field
        
    return type('QuestionForm',(forms.BaseForm,),{'base_fields':fields})


            
            