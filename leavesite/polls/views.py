from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse #tutorial is from django.core.urlresolvers
from .models import Question
# Create your views here.

def index(request): # 3 this will be displayed on http://127.0.0.1:8000/polls
    latest_questions = Question.objects.order_by("-pub_date")[:5] #get all queustions top 5 order by publication date
    # output = ", ".join(q.question_text for q in latest_questions) # loop through all questions and join with "," #static output
    # return HttpResponse("All questions: %s" % output) #static output
    context = {'latest_questions': latest_questions}
    return render(request, 'polls/index.html', context)


def detail(request, question_id):
    # return HttpResponse("This is the details page: %s" % question_id)
    # question = Question.objects.get(pk=question_id)
    question = get_object_or_404(Question, pk=question_id) #handle 404 if question is empty
    context = {'question': question}
    return render(request, 'polls/detail.html', context)

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id) #handle 404 if question is empty
    context = {'question': question}
    return render(request, 'polls/results.html', context)


def vote(request, question_id):
    # return HttpResponse("TVote on questions: %s" % question_id)
    question = get_object_or_404(Question, pk=question_id) #handle 404 if question is empty
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except:
        return render(request, 'polls:details.html', {'question': question, 'error_message':"Please select a choice"})
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
