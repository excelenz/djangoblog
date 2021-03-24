from django.urls import path, include
from  . views import Bot

urlpatterns = [
    path('', Bot.as_view(), name='bot'),
]