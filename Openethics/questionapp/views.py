'''
Created on Jun 26, 2012

@author: ayoola_al
'''
from django.shortcuts import get_object_or_404
from models import *
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
def first_questionset(request, questiongroup_id):
    
    '''
    responsible for processing form for the first questions group e.g prescreening questions
    the first question group are all boolean fields
     
    '''
    #this variable sets the first page of the question!
    
    
    #Q_order = QuestionOrder.objects.get(questiongroup=1)
    #print Q_order.order_info
    
   
    
    
    
    #This need to be fixed, the first questiongroup id should be the one that is being accessed from the 
    #first item in Questionnaire list
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
#            for(question,answer) in formdata:
#                if answer == 'True' :
#                    return HttpResponseRedirect(reverse
#                            ('questionapp.views.other_questionset',request, 
#                                 kwargs={'username': request.user.username}))
#                else:
#                    return HttpResponseRedirect(reverse
#                            ('questionapp.views.success',request, 
#                                 kwargs={'username': request.user.username}))
                    
    else:
        
        return render_to_response('questionform.html', 
                                  {'form': questionForm,},context_instance=RequestContext(request))
   

def success_view(request):
    return render_to_response('success.html') 


def get_next_questionsgroupid(request,order_info):
    '''
    responsible for retrieving  the next questionset to render 
    @return: the next question group id
    '''
    if order_info == 1:
        #move to the first_questionset view!
        return HttpResponseRedirect(reverse('first_questionset', context = order_info ))
        #else count all question group inside a questionnaire
        
    
    else:    
    
        Q_count = QuestionOrder.objects.count()
        print Q_count

        order_info = 1
        
        return HttpResponseRedirect(reverse('first_questionset', context = order_info ))


    
def get_answers(self):
    '''
    return question and answer pair tuple
    
    self.field[name].label is data for the object to be inserted to the QuestionAnswer
    '''
    
    
    for question, answer in self.cleaned_data.items():
        print self.cleaned_data.items()
        yield (question, answer)
        







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
        return render_to_response('questionform.html', 
                                  {'form': questionForm,},context_instance=RequestContext(request))
                





