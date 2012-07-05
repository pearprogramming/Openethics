'''
Created on Jun 26, 2012

@author: ayoola_al

'''

from django import forms
from models import Questiongroup,Questionnaire
from django.forms.fields import CharField,BooleanField,TextField
from views import get_total_questionnaire_questions,get_questionnnaire_name



FIELD_TYPES={
            0: CharField(max_length=100) ,
            1: CharField(widget = forms.Textarea),
            2: BooleanField(initial= False)
            }
def make_question_group_form(thisquestionnaire_grouplist):
    '''
     mapping questions fields  type  to form fields type 
     create form for questionnaire
     @return: type form for given questionnaire
    
    '''
    fields={}
    questionnairename=get_questionnnaire_name

    for questiongroups in [thisquestionnaire_grouplist]:
        thisgroupquestions = Questiongroup.objects.get(pk=questiongroup_id).questions.all()
        
        for question in thisgroupquestions:
            fields[question.label]= FIELD_TYPES[question.field_type]
#        field = FIELD_TYPES[question.field_type] 
#       field.label = question.label
#        fields[str(question.id)]= field
        
    return type('%s Form'% questionnairename,(forms.BaseForm,),{'base_fields':fields})


            
            