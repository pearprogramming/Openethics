'''
Created on 20 Jun 2012

@author: mzd2
'''
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
import models, forms

def prepare_blank_answers(evaluation):
    for question in evaluation.scheme.evaluationquestion_set.all():
        answer = models.EvaluationAnswer(evaluation=evaluation,
                                         question=question)
        answer.save()

def answer_form(request, id):
    evaluation = get_object_or_404(models.Evaluation, id=id)
    if len(evaluation.evaluationanswer_set.all()) == 0:
        prepare_blank_answers(evaluation)
    if request.method == 'POST':
        formset = forms.AnswerFormSet(request.POST, instance=evaluation)
        if formset.is_valid():
            formset.save()
            return HttpResponse('Thank you!')
    else:
        formset = forms.AnswerFormSet(instance=evaluation)
    return render_to_response('answer_form.html',
            {'formset':formset, 'evaluation':evaluation})
    
    
    