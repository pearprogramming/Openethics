'''
Created on Jun 26, 2012

@author: ayoola_al
'''
from django.shortcuts import get_object_or_404
from models import AnswerSet, Question,Questionnaire,AnswerSet,Answers
from forms import make_question_group_form
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.forms import forms
from django.core.urlresolvers import reverse
from django.template import  RequestContext
from django.contrib.auth.models import  User
from django.contrib.auth.decorators import login_required
from questionapp.forms import *

@login_required
def first_questionset(request):
    
    '''
    responsible for processing form for the first questions group e.g prescreening questions
    the first question group are all boolean fields
     
    '''
    #this variable sets the first page of the question!
    questiongroup_id=1
    
    
    user=request.user
    questionForm = make_question_group_form(questiongroup_id)
    
    
    
    if request.method =='POST':  
                 
        form = questionForm(request.POST)
        
        
        if  form.is_valid():
            
            formdata=get_answers(form)
            print formdata
            
            for(question_id,answer) in formdata:
                #save question and answer before redirect
                
                question = get_object_or_404(Question, pk=question_id) 
                
                thisinstance= AnswerSet(user=request.user,
                                question=question,answer=answer)
                
                thisinstance.save()
                #evaluate form fields values if any is true redirect to further questions
                
            return HttpResponseRedirect(reverse('questionapp_success'))    

                    
    else:
        
        return render_to_response('questionform.html', 
                                  {'form': questionForm,},context_instance=RequestContext(request))
   

def success_view(request):
    return render_to_response('success.html') 
    
def get_answers(self):
    '''
    return question and answer pair tuple
    
    '''  
    for question, answer in self.cleaned_data.items():
        yield(question,answer)

def get_total_group_questions(questiongroup_id):
    '''
    @return: total number of questions in the given questiongroup
    '''
    totalcount =  Questiongroup.objects.get(pk=questiongroup_id).questions.all().count()
    return totalcount


def get_total_questionnaire_questions(groupidlist):
    '''
    @return: total number of questions in the questionaire
    '''
    for groupid in groupidlist:
      totalcount =  Questiongroup.objects.get(pk=questiongroup_id).questions.all().count() 
      totalcount += totalcount
    return totalcount

def get_questionnaire_groupidlist(questionnaire_id):
    '''
    @return: list of questiongroups in this questionnaire
    
    '''
    thisquestionnaire=get_object_or_404(Questionnaire,pk=questionnaire_id)
    thisquestionnaire_groups=thisquestionnaire.questiongroups.all()
    thisquestionnaire_grouplist=[]
 
    for qroup in list(thisquestionnaire_groups):
        thisquestionnaire_grouplist.append(group.id)
    
    return thisquestionnaire_grouplist
def get_questionnnaire_name(questionnaire_id):
    '''
    @return: questionnaire name
    '''
    thisquestionnaire=get_object_or_404(Questionnaire,pk=questionnaire_id)
    return thisquestionnaire.name
    
def other_questionset(request,questiongroup_id):
    '''
    view  for processing form for other questionsgroups 
    save the instance and redirect to next question groups
    
    '''
    user=request.user
    
    
    questionForm = make_question_group_form(questiongroup_id=questiongroup_id)
    if request.method =='POST':  
        form = questionForm(request.POST)
        if  form.is_valid():
            formdata=get_answers(form)
            for(question,answer) in formdata:
                #save question and answer before redirect
                thisinstance= AnswerSet(user=request.user,questiongroup_id=questiongroup_id,
                                question=question,answer=answer,status=0)
                thisinstance.save()
        return HttpResponseRedirect(reverse
                            ('questionapp.views.success',request, 
                                 kwargs={'username': request.user.username}))
    else:
        thisquestionnaire_name=get_object_or_404(Questionnaire,pk=questionnaire_id)
        return render_to_response('questionform.html', 
                                  {'form': questionForm,},context_instance=RequestContext(request))
                


def questionnaire_questions(request,questionnaire_id=questionnaire_id):
    '''
      retrieve list of questiongroups for this questionnaire . 
      get the form for the questionnnaire and process form data

    '''
    thisquestionnaire_grouplist = get_questionnaire_groupidlist(questionnaire_id)
#    create dynamicforms for  question groups in this quesnnaire 
    questionnaireForm= make_question_group_form(thisquestionnaire_grouplist)
    #make forsetform for each form
    QuestionnnaireFormset =formset_factory(questionnaireForm)
    
    ALL_VALID=False
    
    if request.method =='POST':
        formset = QuestionnaireFormset(request.POST, request.FILES, prefix='%s_Form' %questionnaire_id)   
                # retrieve each from multiple formset and valid    
        for form in [formset]:
            if form.is_valid():
                for i in xrange(0, get_total_questionnaire_questions(thisquestionnaire)):
                            formdata=get_answers(form)
                            for(question,answer) in formdata:
                #save question and answer before redirect
                                thisinstance= AnswerSet(user=request.user,question=question,answer=answer)
                                thisinstance.save()
                                ALL_VALID=True
           
    
    if (ALL_VALID):
        HttpResponseRedirect(reverse
                            ('questionapp.views.questionnairesuccess',request
                                ))    
    else:
        formset = QuestionnaireFormset()
        for  form in [formset]:
            formset = QuestionsFormset( prefix='%s_Form' %questiongroup_id)
        
    return render_to_response('otherquestionform2.html', 
                                  {'formset':formset},context_instance=RequestContext(request))
    
    
def get_next_questionsgroupid(questiongroup_id):
    '''
    responsible for retrieving  the next questionset to render 
    @return: the next question group id
    '''
    pass   