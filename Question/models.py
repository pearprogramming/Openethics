'''
Created on 20 Jun 2012

@author: mzd2
'''

from django.db import models





RATING_CHOICES = ((0, u"Yes"), (1, u"No"), (2, u"Maybe"),)


    
class EvaluationScheme(models.Model):
    title = models.CharField(max_length=200)




class Evaluation(models.Model):
    doctor = models.CharField(max_length=200)
    agency = models.CharField(max_length=200)
    scheme = models.ForeignKey(EvaluationScheme)

class EvaluationQuestion(models.Model):
    question = models.CharField(max_length=200)
    evaluation = models.ForeignKey(EvaluationScheme)

    def __unicode__(self):
        return self.question



class EvaluationAnswer(models.Model):
    evaluation = models.ForeignKey(Evaluation)
    question = models.ForeignKey(EvaluationQuestion)
    answer = models.SmallIntegerField(choices=RATING_CHOICES)
    
