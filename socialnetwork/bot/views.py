from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
import random
import json
import urllib
import re
import time

# we wanna call to bot by get URL not from console.

class Bot(APIView):

    urlRegister = "http://127.0.0.1:5000/api/token/register/"
    urlGetToken = "http://127.0.0.1:5000/api/token/"

    def get(self, request):
        content = {'message': self.signup()}
        return Response(content)

    def signup(self):
        username =  str(random.randrange(100000, 1000000)) +'user'
        password =  str(random.randrange(100000, 1000000))+'!z34'
        payload = {'email': str(random.randrange(100, 1000))+'asfasf@gmail.com', 'username': username,'password':password }
        r = requests.post(self.urlRegister, data=payload)
        if 'successfully registered new user' in str(r.json()['response']):
            payload = {'username': username,'password':password}
            time.sleep(1)
            token = self.login(**payload)
            return token
        else:
            return {"responce":"we lost"}

    def login(self,**kwargs):
        login_data = {}
        for key in ('username','password'):
            try:
                login_data[key] = kwargs[key]
                setattr(self, key, kwargs[key])
            except:
                setattr(self, key, "")
        print(login_data)
        r = requests.post(self.urlGetToken, data=login_data)
        return {"responce":r,"credentials":login_data}