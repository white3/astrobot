from django.http import HttpResponse
from django.http import JsonResponse
from .core import QuestionHandler
from .models import Question
from .serializers import Sence3Serializer

def chatbot(request):
    return HttpResponse("This is OverSky Chatbot Team, Welcome!")

def ask_question(request):
    response  = {
        'mid': '0000',
        'msg': 'The Sun is so hot.'
    }
    if request.method == 'POST':        
        question_info = Question.objects.filter(msg=request['msg'], mid=request['mid'])
        question  = Sence3Serializer(question_info, many=True, fields=("msg", "mid")).data[0]
        response['msg'] = QuestionHandler().handle(question)
        response['mid'] = '1000'
    return JsonResponse(response)
