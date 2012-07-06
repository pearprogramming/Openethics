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
                
                
                
            
            return HttpResponseRedirect(reverse('get_next_questionsgroupid', kwargs = {'order_info' : order_info}))    
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
    #for now lets use the First Questionnaire
    #quest1 = Questionnaire(name='Questionnaire A B C')
    quest2 = Questionnaire(id=2)
    
    quest = Questionnaire(pk=2)
    
    order_info = int(order_info)    
    
    groups = quest2.questiongroup.all()
    print groups
    correct_order = QuestionOrder.objects.filter(questionnaire=quest2).order_by('order_info')
        
        
    for group in correct_order:
        print group
        actual_group = group.questiongroup
        print actual_group.questiongroupname
        print actual_group.id
        
    #firstquestion = correct_order[0]
        
    #firstquestion_id = firstquestion.id
        
    #print firstquestion.id
        
    if order_info == 1:                
        #get questiongroup_id that has order_info=1 on that group
        questiongroup_id = correct_order[0].questiongroup.id    
        return HttpResponseRedirect(reverse('first_questionset', kwargs = {'questiongroup_id' : questiongroup_id} ))
        
        
    
    else:    
        
        
        
        questiongroup_id = correct_order[order_info].questiongroup.id   
        
        return HttpResponseRedirect(reverse('first_questionset', kwargs = {'questiongroup_id' : questiongroup_id} ))


def get_questionnaire(request,questionnaire_name_id):
    '''
    responsible in calling the questionnaire name, and giving the first one!        
    '''
    
    
    questionnaire_object = Questionnaire(questionnaire_name_id)
    
    order_info = 1
    return HttpResponseRedirect(reverse('questionapp.views.get_next_questiongroupid', kwargs = {'questionnaire_object' : questionnaire_object,
                                                                              'order_info' : order_info
                                                                              } ))
    
    
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
                





