'''
Created on Jun 26, 2012

@author: ayoola_al
'''
from django.db import models
from django.forms import forms

from django.contrib.auth.models import User
from datetime import datetime


class CustomListField(models.TextField):
    '''
    for creating  custom list field override some model.fields methods
    '''
    __metaclass__ = models.SubfieldBase

    def __init__(self, *args, **kwargs):
        self.token = kwargs.pop('token', ',')
    
        kwargs={'default':None,'null':True,'blank':True,'help_text':'Enter option for select Field Type seperated by comma e.g No ,Yes,Not Applicable '}
        
        super(CustomListField, self).__init__(*args, **kwargs)

    def to_python(self, value):
        if not value: return
        if isinstance(value, list):
            return value
        return value.split(self.token)

    def get_db_prep_value(self, value,connection=None,prepared=False):
        if not value: return
        assert(isinstance(value, list) or isinstance(value, tuple))
        return self.token.join([unicode(s) for s in value])

    def value_to_string(self, obj):
        value = self._get_val_from_obj(obj)
        return self.get_db_prep_value(value)
 
class Questiongroup(models.Model):
    '''
    reponsible for question groups ,each group set can have one to  many set of questions 
    order_no store the order or sequence the question group is to be rendered .e.g  order_no = 2 will be rendered before order_no =3  
    '''
    class Meta():
        db_table ='questiongroup'
    questiongroupname = models.CharField('question group name',max_length=255,unique=True)
    
    def __unicode__(self):
        return self.questiongroupname


FIELD_TYPE_CHOICES=(('charfield','charfield'),('textfield','textfield'),('booleanfield','boolean'),('selectfield','select'),)  
  
class Question(models.Model):
    '''
    responsible for storing questions
    define attributes of a question and type of questions e.g boolean ,textfield , charfield
    '''
    class Meta():
        db_table ='question'
    
    label=models.CharField('question',max_length=255)
    field_type=models.CharField(choices=FIELD_TYPE_CHOICES,max_length=100)
    questiongroup=models.ForeignKey(Questiongroup,related_name='questions')
    selectoptions=CustomListField()
    def __unicode__(self):
        return 'Question:%s FieldType:%s Questiongroup:%s Selectoptions:%s' %(self.label, self.field_type,self.questiongroup,self.selectoptions)
    def save(self,*args,**kwgs):
        if not self.id:
          
          if self.field_type == 'selectfield': 
            self.selectoptions = self.selectoptions
            
          else: 
            self.selectoptions = None
        super(Question,self).save(*args,**kwgs)
    
STATUS_TYPES =((0,'completed'),(1,'referred'),(2,'awaiting'),)

 
class AnswerSet(models.Model):
    '''
    this class datamodel for storing users questions and answer 

    '''
    class Meta():
        db_table ='answer_set'
    user=models.ForeignKey(User)
    question=models.ForeignKey(Question)
    answer=models.CharField(max_length=250)
    
    def save(self, *args, **kwargs):                       
        super(AnswerSet, self).save(*args, **kwargs)
        
class Questionnaire(models.Model):
    '''
    This class stores the list of order set
    '''
    name=models.CharField(max_length=250)
    questiongroup=models.ManyToManyField(Questiongroup, through='QuestionOrder')
    
    def __unicode__(self):
        return self.name
    
class QuestionOrder(models.Model):
    '''
    This class stores the ordering of the question rendered on the page
    '''
    questiongroup=models.ForeignKey(Questiongroup)
    questionnaire=models.ForeignKey(Questionnaire)
    order_info=models.IntegerField(max_length=3)
    
    def __unicode__(self):
        return 'group:%s order:%s' %(self.questiongroup, str(self.order_info))

