'''
Created on Jun 26, 2012

@author: ayoola_al
'''
from django.db import models
from django.forms import forms

from django.contrib.auth.models import User
from datetime import datetime
 
class Questiongroup(models.Model):
    '''
    reponsible for question groups ,each group set can have one to  many set of questions 
    order_no store the order or sequence the question group is to be rendered .e.g  order_no = 2 will be rendered before order_no =3  
    '''
    class Meta():
        db_table ='questiongroup'
        verbose_name_plural='Questiongroups'
    questiongroupname = models.CharField('question group name',max_length=255,unique=True)
    
    def __unicode__(self):
        return self.questiongroupname

FIELD_TYPE_CHOICES=((0,'charfield'),(1,'textfield'),(2,'boolean'),)
    
class Question(models.Model):
    '''
    responsible for storing questions
    define attributes of a question and type of questions e.g boolean ,textfield , charfield
    '''
    class Meta():
        db_table ='question'
        
    
    label=models.CharField('question',max_length=255)
    field_type=models.IntegerField(choices=FIELD_TYPE_CHOICES)
    questiongroup=models.ForeignKey(Questiongroup,related_name='questions')
   
    def __unicode__(self):
        return self.label
    
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

class Answers(models.Model):
    answerset=models.ForeignKey('AnswerSet',related_name='answers')
            
class Questionnaire(models.Model):
    '''
    This class stores the list of questionnaire set
    '''
    class Meta():
        db_table='questionnaire'
        verbose_name_plural='questionnaires'
    name=models.CharField(max_length=250)
    questiongroups=models.ManyToManyField(Questiongroup,through='Questionnaire_Questiongroup')   
    
    def __unicode__(self):
            return self.name
class Questionnaire_Questiongroup(models.Model):
    '''
    define the association betwen Questionaire and Questiongroup 
    
    '''
    class meta():
        db_table='Questionnaire_Questiongroup'
    questionnaire= models.ForeignKey(Questionnaire)
    questiongroup= models.ForeignKey(Questiongroup)
