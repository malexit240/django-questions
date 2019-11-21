from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect
from .models import Question, Choice
from django.template import loader
from django.shortcuts import render,get_object_or_404
from django.urls import reverse

def index(request):
    return render(request,'polls/index.html',{
        "lastest_question_list":Question.objects.order_by('-pub_date')[:5]
    })

    lastest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        "lastest_question_list":lastest_question_list
    }
    return HttpResponse(template.render(context,request))

def detail(request,question_id):
    try:
        return render(request,'polls/details.html',{
        "question":Question.objects.get(id=question_id)
    })
    except Question.DoesNotExist:
        raise Http404('Question does')



def result(request, question_id):
    question = get_object_or_404(Question,pk=question_id)

    return render(request,'polls/result.html',{"question":question})

def vote(request, question_id):
    question = get_object_or_404(Question,id=question_id)
    try:
        selected_choice = question.choice_set.get(id=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        pass
    else:
        selected_choice.votes +=1
        selected_choice.save()

        return HttpResponseRedirect('result'.format(question_id))
