from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response


class Bot(APIView):
    def get(self, request):
        content = {'message': 'Ok'}
        return Response(content)
