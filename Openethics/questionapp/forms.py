'''
Created on Jun 26, 2012

@author: ayoola_al

'''

from django import forms
from models import Questiongroup,Questionnaire
from django.forms.fields import CharField,BooleanField




FIELD_TYPES={
            0: CharField(max_length=100) ,
            1: CharField(widget = forms.Textarea),
            2: BooleanField(initial= False)
            }
def make_question_group_form(thisquestionnairename,thisquestionnaire_grouplist):
    '''
     mapping questions fields  type  to form fields type 
     create form for questionnaire
     @return: type form for given questionnaire
    
    '''
    fields={}
    questionnairename=thisquestionnairename

    for questiongroup_id in thisquestionnaire_grouplist:
        thisgroupquestions = Questiongroup.objects.get(pk=questiongroup_id).questions.all().order_by('label')
        
        for question in thisgroupquestions:
            fields[question.label]= FIELD_TYPES[question.field_type]
#        field = FIELD_TYPES[question.field_type] 
#       field.label = question.label
#        fields[str(question.id)]= field
        
    return type('%s Form' % str(questionnairename),(forms.BaseForm,),{'base_fields':fields})


            
            