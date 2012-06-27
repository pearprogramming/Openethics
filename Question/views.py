'''
Created on 20 Jun 2012

@author: mzd2
'''
from django.http import HttpResponse
from django.shortcuts import render_to_response, get_object_or_404
import models, forms
from django.views.generic import list_detail
from Question.models import *

def prepare_blank_answers(evaluation):
    for question in evaluation.Set.evaluationquestion_set.all():
        answer = models.EvaluationAnswer(evaluation=evaluation,
                                         question=question)
        answer.save()

       


def answer_form(request, id):
    evaluation = get_object_or_404(models.User, id=id)
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
    
    

def Prescreen(request):
    return list_detail.object_list(
        request,
        queryset=PrescreenQuestion.objects.all(),
        paginate_by=20,
    )
Prescreen.__doc__ = list_detail.object_list.__doc__


def QuestionSetList(request):
    return list_detail.object_list(
        request,
        queryset=QuestionSetList.objects.all(),
        paginate_by=20,
    )
QuestionSetList.__doc__ = list_detail.object_list.__doc__


