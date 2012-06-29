'''
Created on Jun 26, 2012

@author: ayoola_al

'''
from django.forms import forms
from django import forms
from models import *
from django.forms.fields import *



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
    thisgroupquestions = Questiongroup.objects.get(id=questiongroup_id).questions.all()

    
    fields={}
    #for question in scheme.questions.all():
    for question in thisgroupquestions:

        
        fields[question.label]= FIELD_TYPES[question.field_type]
        
        
      
    return type('QuestionForm',(forms.BaseForm,),{'base_fields':fields})


            
            