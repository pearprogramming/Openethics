'''
Created on 20 Jun 2012

@author: mzd2
'''

from django.db import models





RATING_CHOICES = ((0, u"Yes"), (1, u"No"), )

#(2, u"Maybe"),

# PrescreenQuestion, Question is built based on what has been selected yes!  
class PrescreenQuestion(models.Model):
    PreQuestion = models.CharField(max_length=200)
    PreQuestionFlag = models.SmallIntegerField(choices=RATING_CHOICES)
    
    
    def __unicode__(self):
        return u"%s" % self.PreQuestion

#Each Prescreen Question is linked to one Question Set
class QuestionSet(models.Model):
    title = models.CharField(max_length=200)
    PreQuestion = models.ForeignKey(PrescreenQuestion)

    def __unicode__(self):
        return u"%s" % self.title


#Each Question in Question Bank will have one or more relationship with QuestionSet
class QuestionBank(models.Model):
    question = models.CharField(max_length=200)
    QSet = models.ForeignKey(QuestionSet)

    def __unicode__(self):
        return self.question
    
    
class Answer(models.Model):
    question = models.ForeignKey(QuestionBank)
    answer = models.SmallIntegerField(choices=RATING_CHOICES)



    
class User(models.Model):
    User = models.CharField(max_length=200)
    Type = models.CharField(max_length=200)
    Set = models.ForeignKey(QuestionSet)
    
    def __unicode__(self):
        return u"%s" % self.User

class EvaluationAnswer(models.Model):
    evaluation = models.ForeignKey(User)
    question = models.ForeignKey(QuestionBank)
    answer = models.SmallIntegerField(choices=RATING_CHOICES)
    
    
