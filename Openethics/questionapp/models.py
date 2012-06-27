'''
Created on 25 Jun 2012

@author: ala23
'''

from django.db import models
from django.forms import forms


class Scheme(models.Model):
    '''
    for questions scheme ,each scheme can one to many questions
    '''
    name= models.CharField(max_length=255)
    #schemeID= models.PositiveIntegerField(unique=True)
    scheme_date = models.DateTimeField('date created')
    
    def __unicode__(self):
        return self.name

FIELD_TYPE_CHOICES=((0,'charfield'), (1,'textfield'),(2,'boolean'),)


class Question(models.Model):
    '''
    responsible for storing question
    defines  attribute of a question and type of question e.g boolean ,textfield ,charfield
    '''
    scheme=models.ForeignKey(Scheme,related_name='questions')
    label= models.CharField(max_length=255)
    field_type=models.IntegerField(choices=FIELD_TYPE_CHOICES)

FIELD_TYPES={0:'forms.Charfield',
            1:'forms.Charfield(widget=forms.Textarea)',
            2:'forms.BooleanField',}
def form_question_scheme(scheme):
    '''
    mapping questions to the type of form fields @return: form filed
    '''
    fields={}
    for question in scheme.questions.all():
        fields[question.label]=FIELD_TYPES[question.field_type](label=question.label)
        return type('%Form' %scheme.name,(forms.Form,),fields)
    
    
class UserQA(models.Model):
    '''
    reponsible to storing of user questions and answers to a specific schmeme
    '''
    
                                                    
    
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
