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
        print user
        
        
        form = questionForm(request.POST)
        if  form.is_valid():
            
            formdata=get_answers(form)
            
            
            for(question_id,answer) in formdata:
                #save question and answer before redirect

                
                question = get_object_or_404(Question, pk=question_id) 
                thisinstance= AnswerSet(user=request.user,
                                question=question,answer=answer)
                thisinstance.save()

            order_info = 2
            return HttpResponseRedirect(reverse('questionapp_success'))
            #return HttpResponseRedirect(reverse('get_questionsgroupid', kwargs = {'order_info' : order_info}))    
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



def get_next_questionsgroupid(request,order_info,questionnaire):
    '''
    responsible for retrieving  the next questionset to render 
    @return: the next question group id
    '''
    #for now lets use the First Questionnaire
    #quest1 = Questionnaire(name='Questionnaire A B C')
    order_info = int(order_info)    
    questionnaire = int(questionnaire)      
    quest = Questionnaire(id=questionnaire)
    correct_order = QuestionOrder.objects.filter(questionnaire=quest).order_by('order_info')
      
    if order_info == 1:                
        #get questiongroup_id that has order_info=1 on that group
        questiongroup_id = int(correct_order[0].questiongroup.id)            
        return HttpResponseRedirect(reverse('first_questionset',  kwargs = {'questiongroup_id' : questiongroup_id} ))   
    else:
        order_info = order_info - 1           
        questiongroup_id = correct_order[order_info].questiongroup.id        
        return HttpResponseRedirect(reverse('first_questionset',  kwargs = {'questiongroup_id' : questiongroup_id} ))


def get_questionnaire(request,questionnaire_id):
    '''
    responsible in calling the questionnaire name, and giving the first question in order = 1!        
    '''
    questionnaire = int(questionnaire_id)    
    
    order_info = 1
    return HttpResponseRedirect(reverse('get_questionsgroupid', kwargs = { 'order_info' : order_info , 'questionnaire' : questionnaire  } ))
    
    
def get_answers(self):
    '''
    return question and answer pair tuple
    
    self.field[name].label is data for the object to be inserted to the QuestionAnswer
    '''  
    for question, answer in self.cleaned_data.items():
        print self.cleaned_data.items()
        yield (question, answer)
        







