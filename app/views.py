from django.http import HttpResponse, HttpResponseRedirect
from django.template import Context, RequestContext, loader
from django.shortcuts import render_to_response
# import application models
# stored in __init__.py file
from app import * 

def home(request):
    questions_list = Question.objects.all()
    l = loader.get_template('app/index.html')
    c = Context({'questions_list': questions_list})
    return HttpResponse(l.render(c))

def question(request, question_id):
    arguments = {'question': Question.objects(id=question_id)[0]}
    return render_to_response('app/detail.html', arguments, context_instance=RequestContext(request))

def answer(request, question_id):
    q = Question.objects(id=question_id)[0]
    a = Answer()
    a.author = Author(name = request.POST["author_name"], email=request.POST["author_email"])
    a.content = request.POST["answer_content"]
    q.answers.appent(a)
    q.save()
    return HttpResponseRedirect('/' + str(question_id))

def new(request):
    return render_to_response('app/create.html', {}, context_instance=RequestContext(request))

def create(request):
    q = Question()
    q.title = request.POST["title"]
    q.content = request.POST["content"]
    q.author = Author(name=request.POST["author_name"], email=request.POST["author_email"]) 
    q.tags = request.POST["tags"]
    q.save()
    return HttpResponseRedirect('/' + str(q.id))
