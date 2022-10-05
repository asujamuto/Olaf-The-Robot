from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from chatbot import RobotWarsaw

from main.forms import MessageForm


def talk(message):
    robot1 = RobotWarsaw()
    answer1 = robot1.answer(message)
    return answer1


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



