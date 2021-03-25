from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
import requests
import random
import json
import urllib
import re
import time
import os

# we wanna call to bot by get URL not from console.

class Bot(APIView):

    urlRegister = "http://127.0.0.1:5000/api/token/register/"
    urlGetToken = "http://127.0.0.1:5000/api/token/"
    urlPostArticle = "http://127.0.0.1:5000/api/token/post/"
    module_dir = os.path.abspath(os.path.dirname(__file__+ "/../../"))
    with open(os.path.join(module_dir,'static/setbot.txt')) as fp:
       line = fp.readline()
       cnt = 1
       sets = {}
       while line:
           x = line.replace('\n', '').replace(' ', '').split("=")
           sets[x[0]]=x[1]
           line = fp.readline()

    def get(self, request):
        content = []
        [content.append(self.make_user()) for i in range(int(self.sets['number_of_users']))]
        return  Response(content)

    def make_user(self):
        signup  =  self.signup()
        time.sleep(1)
        if signup['status']==1:
            payload = {'username': signup['username'] ,'password':signup['password']}
            token = self.login(**payload)
            content = {'credentials': signup,'token':token}
        else:
            return {"status":"fail"}
        return content


    def signup(self):
        username =  str(random.randrange(100000, 1000000)) +'user'
        password =  str(random.randrange(100000, 1000000))+'!z34'
        payload = {'email': str(random.randrange(100, 1000))+'asfasf@gmail.com', 'username': username,'password':password }
        r = requests.post(self.urlRegister, data=payload)
        if 'successfully registered new user' in str(r.json()['response']):
            payload['status'] = 1
            return payload
        else:
            return {"status":"0"}

    def login(self,**kwargs):
        login_data = {}
        for key in ('username','password'):
            try:
                login_data[key] = kwargs[key]
                setattr(self, key, kwargs[key])
            except:
                setattr(self, key, "")
        r = requests.post(self.urlGetToken, data=login_data)
        mylist1 = ["ראטארט", "ראטארטאט", "ארטרטאטארט"]
        mylist2 = ["dsfdsfdsafdsafdsafdsafdsfdsfs", "rsdfdsafdsfdsדגכדגכגדכגדכגדכtrtrtfor", "pytrדגכגדכגדכגדכגדכגדכגדכגדכtrtrtrtrhon"]
        [self.autopost(**{'title': random.choices(mylist1) ,'author': login_data['username'] ,'status':1,'content': random.choices(mylist2) , 'key': r}) for i in range(int(self.sets['max_posts_per_user']))]
        return r

    def autopost(self,**kwargs):
        login_data = {}
        for key in ('title','author','status','content','key'):
            try:
                login_data[key] = kwargs[key]
                setattr(self, key, kwargs[key])
            except:
                setattr(self, key, "")
        r = requests.post(self.urlPostArticle, data=login_data)
        return 1
