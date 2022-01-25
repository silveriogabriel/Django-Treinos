from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    context = {'latest_question_list': latest_question_list}
    return render(request, 'polls/index.html', context)

def detail(request, question_id):
    return HttpResponse(f'Essa é a pergunta de numero {question_id}.')

def results (request, question_id):
    response = (f'Estes são os resultados da pergunta {question_id}.')
    return HttpResponse(response)

def vote(request, question_id):
    return HttpResponse(f'Você votou na pergunta {question_id}.')
