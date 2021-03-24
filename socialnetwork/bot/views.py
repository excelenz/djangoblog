from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
import random
import json
import urllib
import re

# we wanna call to bot by get URL not from console.

class Bot(APIView):

    urlRegister = "http://127.0.0.1:5000/api/token/register/"

    def get(self, request):

        content = {'message': self.signup()}
        return Response(content)

    def signup(self):
        payload = {'email': str(random.randrange(100, 1000))+'asfasf@gmail.com', 'username': str(random.randrange(100000, 1000000)) +'user','password': str(random.randrange(100000, 1000000))+'!z34'}
        r = requests.post(self.urlRegister, data=payload)
        return r
