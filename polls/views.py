from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import render
from .models import Question


def index(request):
    print('****** SCRIPT_NAME: ' + request.META['SCRIPT_NAME'] + '*******')
    print('****** STATIC_URL: ' + settings.STATIC_URL + '*******')
    print('****** COMPRESS_URL: ' + settings.COMPRESS_URL + '*******')
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    return render(request, 'polls/index.html', {'questions': latest_question_list})


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
