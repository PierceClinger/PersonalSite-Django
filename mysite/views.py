from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from django.http import JsonResponse
import json
from .chatbot.chatbot import *

def index(request):
    return render(request, "index.html")

def email(request):
    return render(request, "email.html")

def email_submit(request):
    return render(request, "email_submit.html")

def projects(request):
    return render(request, "projects.html")

def chatbot(request):
    if request.method == 'POST':
        question = json.load(request)['message']
        answer = logic(question)
        data = {
            'message':answer,
        }
        return JsonResponse(data)
    return render(request, "chat.html")