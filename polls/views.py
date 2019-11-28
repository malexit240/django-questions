from django.shortcuts import render
from django.http import (HttpResponse, Http404,
                         HttpResponseRedirect, HttpRequest)
from .models import Question, Choice
from django.template import loader
from django.shortcuts import get_object_or_404
from django.views.decorators.http import require_GET
from django.views.generic import ListView, DetailView
from .forms import QuestionForm


class IndexView(ListView):
    template_name = 'polls/index.html'  # model = Question
    context_object_name = 'object_list'
    queryset = Question.objects.order_by('-question_text')


class DetailsView(DetailView):
    template_name = 'polls/details.html'
    model = Question
    context_object_name = 'question'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = QuestionForm()
        return context


class ChoiceCreate(CreateView):
    template_name = 'polls/detail.html'
    model = Choice
    fields = ['question','choice_text']


@require_GET
def index(request: HttpRequest):
    return render(request, 'polls/index.html', {
        "lastest_question_list": Question.objects.order_by('-pub_date')[:5]
    })

    lastest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        "lastest_question_list": lastest_question_list
    }
    return HttpResponse(template.render(context, request))


def detail(request, question_id):
    try:
        return render(request, 'polls/details.html',
                      {"question": Question.objects.get(id=question_id)})
    except Question.DoesNotExist:
        raise Http404('Question does')



def result(request, question_id):
    question = get_object_or_404(Question,pk=question_id)

    return render(request,'polls/result.html',{"question":question})

def vote(request, question_id):
    question = get_object_or_404(Question,id=question_id)

    form = QuestionForm(request.POST)

    if form.is_valid():
        try:
            selected_choice = question.choice_set.get(id=request.POST['choice'])
        except (KeyError, Choice.DoesNotExist):
            pass
        else:
            selected_choice.votes +=1
            selected_choice.save()

            return HttpResponseRedirect('{}/result'.format(question_id))


class ChoiceFormView(FormView):
    template_name = 'polls/detail.html'
    form_class = ChoiceModelForm
    succsess_url = '/polls'