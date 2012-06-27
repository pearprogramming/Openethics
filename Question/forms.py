'''
Created on 20 Jun 2012

@author: mzd2
'''
from django.forms.models import inlineformset_factory
import models

AnswerFormSet = inlineformset_factory(models.User, 
        models.EvaluationAnswer, exclude=('question',), 
        extra=0, can_delete=False)

