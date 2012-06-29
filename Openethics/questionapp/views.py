'''
Created on Jun 26, 2012

@author: ayoola_al
'''
from models import *
from forms import *
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.forms import forms
from django.core.urlresolvers import reverse
from django.template import  RequestContext
from django.contrib.auth.models import  User
from django.contrib.auth.decorators import login_required
from questionapp.forms import *

@login_required
def first_questionset(request,questiongroup_id):
    #scheme=Scheme.objects.get(pk=scheme_id)
    '''
    responsible for processing form for the first questions group e.g prescreening questions
    the first question group are all boolean fields
     
    '''
    user=request.user
    questionForm = make_question_group_form(questiongroup_id=1)
    if request.method =='POST':  
        form = questionForm(request.POST)
        if  form.is_valid():
            formdata=get_answers(form)
            for(question,answer) in formdata:
                #save question and answer before redirect
                thisinstance= QuestionAnswer(user=request.user,questiongroup_id=questiongroup_id,
                                question=question,answer=answer,status='awaiting')
                thisinstance.save()
                #evaluate form fields values if any is true redirect to further questions
            for(question,answer) in formdata:  
                if answer == 'True' :
                        return HttpResponseRedirect(reverse
                            ('questionapp.views.other_questionset',request, 
                                 kwargs={'username': request.user.username}))
                else:
                    return HttpResponseRedirect(reverse
                            ('questionapp.views.success',request, 
                                 kwargs={'username': request.user.username}))
                    
    else:
        return render_to_response('questionform.html', 
                                  {'form': questionForm,},context_instance=RequestContext(request))
   
   
   
def other_questionset(request,group_id):
    '''
    view  for processing form for other questionsgroups 
    save the instance and redirect to next question groups
    
    '''
    user=request.user
    questionForm = make_question_group_form(group_id=group_id)
    if request.method =='POST':  
        form = questionForm(request.POST)
        if  form.is_valid():
            formdata=get_answers(form)
            for(question,answer) in formdata:
                #save question and answer before redirect
                thisinstance= QuestionAnswer(user=request.user,group_id=group_id,
                                question=question,answer=answer,status='awaiting')
                thisinstance.save()
        return HttpResponseRedirect(reverse
                            ('questionapp.views.success',request, 
                                 kwargs={'username': request.user.username}))
    else:
        return render_to_response('questionform.html', 
                                  {'form': questionForm,},context_instance=RequestContext(request))
                

def get_next_questionsgroupid(group_id):
    '''
    responsible for retrieving  the next questionset to render 
    @return: the next question group id
    '''
    pass
    

def get_answers(self):
    '''
    return question and answer pair tuple
    
    self.field[name].label is data for the object to be inserted to the QuestionAnswer
    '''
    for name, value in self.cleaned_data.items():
        yield (self.fields[name].label, value)
        