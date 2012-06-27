'''
Created on 25 Jun 2012

@author: ala23
'''
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



def show_questions(request,scheme_id):
    '''
     will be responsible  for boolean form field validation e.g presceening questions 
    '''
    #scheme=Scheme.objects.get(pk=scheme_id)
    user=request.user.id
    schemeForm = make_question_scheme_form(scheme_id)
    if request.method =='POST':  
        
        form = schemeForm(request.POST)
        if  form.is_valid():
            for(question,answer) in form.get_answers():
                # put saving code hear  create instance of data  model  associated with request.user  and save form fileds data  i.e question and answer etc before redirect
                if answer == True :
                    return HttpResponseRedirect(reverse
                            ('questionapp.views.postscreen_questions',request, 
                                 kwargs={'username': request.user.username}))
                else:
                    return HttpResponseRedirect(reverse
                            ('questionapp.views.success',request, 
                                 kwargs={'username': request.user.username}))
    else:
        return render_to_response('schemeform.html', 
                                  {'form': schemeForm,},context_instance=RequestContext(request))
        
                

def other_questions(request,scheme_id):
    '''
    will be responsible  all other questionsets , form validation and save form data a  data model associated with user
    '''
    #scheme=Scheme.objects.get(pk=scheme_id)
    user=request.user.id
    schemeForm = make_question_scheme_form(scheme_id)
    if request.method =='POST':  
        
        form = schemeForm(request.POST)
        if  form.is_valid():
            for(question,answer) in form.get_answers():
                # put saving code hear  create instance of a data model with user instance  save question and answer before redirect
 
                    return HttpResponseRedirect(reverse
                            ('questionapp.views.success',request, 
                                 {'username': request.user.username}))
    else:
        return render_to_response('schemeform.html', 
                                  {'form': schemeForm,},context_instance=RequestContext(request))
        

                
def get_answers(self):
    '''
    return question and answer pair tuple
    '''
    for name, value in self.cleaned_data.items():
        yield (self.fields[name].label, value)