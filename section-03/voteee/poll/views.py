from django.shortcuts import render, get_object_or_404
from django.template import loader
from django.http import HttpResponse, Http404
from poll.models import Question

# Create your views here.
def index(request):
    latest_questions = Question.objects.order_by('-id')[:4]
    template = loader.get_template('poll/index.html')
    context = { "latest_questions_list" : latest_questions }
    # return HttpResponse(" - ".join([str(question.text) for question in top_two_questions]))
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    # try:
    #     question = Question.objects.get(pk=question_id)
    # except Question.DoesNotExist:
    #     raise Http404('Question is not found, id is invalid or nonexistent')
    question = get_object_or_404(Question, pk=question_id)
    context = { "question" : question }
    return render(request, 'poll/question.html', context)

def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)

def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
