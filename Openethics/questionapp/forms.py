'''
Created on Jun 26, 2012

@author: ayoola_al

'''

from django import forms
from models import QuestionGroup,Question_order
from django.forms.fields import CharField,BooleanField,ChoiceField
from django.utils.datastructures import SortedDict
from django.forms.widgets import RadioSelect


class CustomError(Exception):
       def __init__(self, value):
         self.value = value
       def __str__(self):
         return repr(self.value)

def get_choices(question):
    '''
     @return: choices for a given select type question
    '''
    try: 
        choices_list = question.selectoptions
        choices= [(x,x) for x in choices_list]
        return choices
    except CustomError as e:
         msg='Exception has occurred not a valid List : s%' % e.value
         raise MyError(msg)

def generate_charfield():
    '''
     @return charfield ,you can change the default attribute
    '''
    return CharField(max_length=100,widget=forms.TextInput(attrs={'size':'40'}))

def generate_textfield():
    return CharField(widget = forms.Textarea(attrs={'rows':'4','cols':'40',}))

def generate_boolean_field():
    return BooleanField(initial= False)

def generate_selectfield_field():
    '''
    @return: return form ChoiceField
     
    '''
    return ChoiceField(choices=[])

def generate_radioselect_field():
   '''
    @return radioselect field
   ''' 
   return ChoiceField(widget=RadioSelect,choices=[])


FIELD_TYPES={
            'charfield': generate_charfield ,
            'textfield': generate_textfield,
            'booleanfield': generate_boolean_field,
            'selectfield':generate_selectfield_field,
            'radioselect':generate_radioselect_field,
            }


def make_question_group_form(questiongroup_id,questionnairename):
    '''
     dynamically mapping questions fields  types  to form fields type 
     @return: type form for specific questiongroup 
    
    '''
    
    fields = SortedDict([])
    thisgroupquestions = QuestionGroup.objects.get(id=questiongroup_id).questions.all()
    
    for question in thisgroupquestions:
        if question.field_type == 'selectfield' or question.field_type == 'radioselect' :
           tempfield=FIELD_TYPES[question.field_type]()
           tempfield.choices=get_choices(question)
           field=tempfield
           field.label = question.label
           fields[str(question.id)]= field
        else:    
            field = FIELD_TYPES[question.field_type]()
            field.label = question.label
            fields[str(question.id)]= field
        
    return type('%sForm' % str(questionnairename),(forms.BaseForm,),{'base_fields':fields})

         