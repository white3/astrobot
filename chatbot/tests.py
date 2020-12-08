from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from .models import Question
from .serializers import Sence3Serializer
from .core import Handler

class MyTestCase(APITestCase):
    def get(self, url=None):
        return self.client.get(url)

    def post(self, payload, url=None):
        return self.client.post(url)

    def test_serilizer(self):
        question_info = Question.objects.filter(msg="1", mid="0000").all()
        question  = Sence3Serializer(question_info, many=True, fields=("msg", "mid")).data[0]
        self.assertEqual(question['msg'], '1')
        response['msg'] = Handler().handle(question)
        self.assertEqual(response['msg'], '1 is answered.')

    def test_root(self):
        response = self.get('/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_question(self):
        payload = {
            'mid' : '0000',
            'msg' : 'What is the Sun?',
        }
        response = self.post(url='/chatbot_astro_question/', payload=payload)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
#        payload['msg'] += 'is answered.'
#        self.assertEqual(response.content, payload)

