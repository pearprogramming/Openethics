'''
Created on Jun 26, 2012

@author: ayoola_al
'''
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.core.urlresolvers import reverse
from models import QuestionGroup_order, Questionnaire,QuestionGroup,AnswerSet,QuestionAnswer,Question
from django.template import  RequestContext
from django.shortcuts import render_to_response
from forms import make_question_group_form
from django.core.paginator import Paginator, InvalidPage, EmptyPage

def index (request):
    return HttpResponseRedirect(reverse('index'))



def get_next_questiongroup(request,questionnaire_id,order_info=None):
#    retrieve questionnaire object please dont touch this two lines for now
    this_questionnaire= get_questionnnaire_obj(questionnaire_id)
    this_questionnaire_name=get_questionnnaire_name(questionnaire_id)
    
    questionnaire_id = int(questionnaire_id)
    
    if order_info==None:
        order_info = 1

    else:
        order_info = int(order_info)
        
    quest = Questionnaire.objects.get(pk=questionnaire_id)
    orderedgroups = quest.get_ordered_groups()
    
    #below prints the questiongroup id! so it can be used to render a group!
    questiongroup_id = orderedgroups[order_info-1].questiongroup.id    
    
    questionForm = make_question_group_form(questiongroup_id,this_questionnaire_name)
    
    if request.method =='POST':
        
        if order_info == orderedgroups.count():
            this = 'this is the last one!'
            print this
            return HttpResponseRedirect(reverse('questionnaire_finish'))
            
        else:
            
            order_info = order_info + 1
#           this handle the validation and cleaning of all form data using django validation 
#           if you want to do custom validation you have overwrite django's and put what you require from each for form field
            form=questionForm(request.POST)
            if form.is_valid():
                    formdata=get_answers(form)
                    for question,answer in formdata:
                      this_answer_set= AnswerSet(user=request.user,questionnaire=this_questionnaire)
                      this_answer_set.save()
                      this_question_answer=QuestionAnswer(question=get_question_obj(question),answer=answer,answer_set=this_answer_set)
                      this_question_answer.save()
                                    
            return HttpResponseRedirect(reverse('get_next_questiongroup', kwargs = {'questionnaire_id': questionnaire_id, 'order_info' : order_info}))
    
    else:
        return render_to_response('questionform.html', 
        {'form': questionForm,'thisquestionnairename':this_questionnaire_name,'questionnaire_id':questionnaire_id,},context_instance=RequestContext(request))
   

def finish(request):
    return render_to_response('finish.html') 

def display_question_answer(request,questionnaire_id):
    if request.method=='GET':
        user=request.user
        questionanswer=QuestionAnswer.objects.values()
        paginator = Paginator(questionanswer, 2)  
        context=questionanswer
        print context
    return render_to_response('questionanswer.html',{'context':context,},context_instance=RequestContext(request))
         

#This is from the old view, I just left it here maybe you want to improve it based on this

# some helper functions for form data processing etc

def get_answers(self):
    '''
    return question and answer pair tuple
    
     clean data to be inserted to the QuestionAnswer
     using the very basic django for validation. 
     form can ony get here if form is valid
     
    '''  
    for question, answer in self.cleaned_data.items():
        
        yield (question, answer)
        

def get_total_group_questions(questiongroup_id):
    '''
    @return: total number of questions in the given questiongroup
    '''
    totalcount =  QuestionGroup.objects.get(pk=questiongroup_id).questions.all().count()
    return totalcount


def get_questionnnaire_obj(questionnaire_id):
    '''
    @return: questionnaire instance
    '''
    thisquestionnaire=get_object_or_404(Questionnaire,pk=questionnaire_id)
    
    return thisquestionnaire

def get_questionnnaire_name(questionnaire_id):
    '''
    @return: questionnaire name
    '''
    thisquestionnaire=get_object_or_404(Questionnaire,pk=questionnaire_id)
    
    return thisquestionnaire.name

def get_question_obj(question_id):
    '''
    @return: question object instance
    '''
    thisquestion=get_object_or_404(Question,pk=question_id)
    
    return thisquestion

def get_question_name(question_id):
    '''
    @return: question this question label actual question
    '''
    thisquestion=get_object_or_404(Question,pk=question_id)
    
    return thisquestion.label



