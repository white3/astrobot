from django.http import HttpResponse
from django.http import JsonResponse
from .core import Handler
from .models import Question
from .serializers import QuestionSerializer
import json
import pprint

def chatbot(request):
    return HttpResponse("This is OverSky Chatbot Team, Welcome!")

def ask_question(request):
    resp  = {
        'mid': '0000',
        'msg': 'The Sun is so hot.'
    }
    if request.method == 'POST':
        print(request.POST)
        print(request.POST['msg'])
        if request.POST['mid'] == '0000':
            question_info = Question.objects.create(msg=request.POST['msg'], mid=request.POST['mid'])
        resp['msg'] = Handler().handle(question_info)
        resp['mid'] = '1000'
 #   serializer = QuestionSerializer(data=resp, many=True) TODO Safe work
    return JsonResponse(json.dumps(resp), safe=False)
