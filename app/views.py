from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, RequestContext, loader
from django.shortcuts import render_to_response
# import application models
# stored in __init__.py file
from app import * 
from app.forms import *

# import for reading binary file
from PIL import Image
import StringIO
from math import sqrt

def home(request):
    questions_list = Question.objects.all()
    l = loader.get_template('app/index.html')
    c = Context({'questions_list': questions_list})
    return HttpResponse(l.render(c))

def question(request, question_id):
    arguments = {'question': Question.objects(id=question_id)[0]}
    print Question.objects(id=question_id)[0].author
    return render_to_response('app/question.html', arguments, context_instance=RequestContext(request))

def answer(request, question_id):
    q = Question.objects(id=question_id)[0]
    a = Answer()
    ar = Author(name = request.POST["author_name"], email=request.POST["author_email"])
    ar.save()
    a.author = ar
    a.content = request.POST["answer_content"]
    q.answers.append(a)
    print q.answers[0].content
    q.save()
    return HttpResponseRedirect('/' + str(question_id))

def new(request):
    return render_to_response('app/create.html', {}, context_instance=RequestContext(request))

def create(request):
    q = Question()
    q.save()
    q.title = request.POST["title"]
    q.content = request.POST["content"]
    a = Author(name=request.POST["author_name"], email=request.POST["author_email"])
    a.save()
    q.author = a;
    q.tags = request.POST["tags"].split()
    q.attachment.put(request.FILES["my_file"], content_type='text')
    q.save()
    return HttpResponseRedirect('/')

def confirm(request, question_id):
    question = Question.objects(id=question_id)[0]
    l = loader.get_template('app/delete.html')
    c = Context({'question': question})
    return HttpResponse(l.render(c)) 

def delete(request, question_id):
    q = Question.objects(id=question_id)[0]
    q.delete()
    return HttpResponseRedirect('/')

def show_file(request, question_id):
    return HttpResponse(Question.objects(id=question_id)[0].attachment.read())
