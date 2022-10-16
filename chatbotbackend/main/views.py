from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from chatbot import RobotWarsaw

from main.forms import MessageForm
from main.forms import EmailForm

from main.models import Conversation

import sqlite3

from django.core.mail import send_mail


def talk(message):
    robot1 = RobotWarsaw()
    answer, tag = robot1.answer(message)

    conv_data = Conversation()

    conv_data.user_message = message
    conv_data.bot_message = answer
    conv_data.tag = tag

    conv_data.save()

    return answer



def send(response):
    return render(response, "main/send_email.html")

def email_form(response):
    if response.method == "POST":
        form = EmailForm(response.POST)
        if form.is_valid():
            data = form.cleaned_data
            send_mail('Hello from Robot!',str(data["user"]),'json.robot27@gmail.com',['sokolowskipiotr297@protonmail.com'])
            return HttpResponse('<h1>Email został wysłany</h1>')
            
    else:
        form = MessageForm()
    return render(response, "main/email_form.html", {"form":form})


def index(response):
    if response.method == "POST":
        form = MessageForm(response.POST)
        
        if form.is_valid():
            data = form.cleaned_data
            answer = talk(data["user"])
        return render(response, "main/home.html", {"form":form, "user_message":data["user"], "bot_message": str(answer)})

            
    else:
        form = MessageForm()
    return render(response, "main/home.html", {"form":form})



