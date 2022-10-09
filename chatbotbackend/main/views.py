from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from chatbot import RobotWarsaw

from main.forms import MessageForm

import sqlite3

def talk(message):
    robot1 = RobotWarsaw()
    answer, tag = robot1.answer(message)

    db = sqlite3.connect("/home/pete/Coding/Python/Artificial_Inteligence/chatbot/databases/sqlite3/message_data.db")
    cursor = db.cursor()
    print(db)
    cursor.execute(" INSERT INTO conversation_data(user_message,tag,bot_answer) VALUES (?, ?, ?)", (str(message),str(tag),str(answer)))
    db.commit()
    db.close()

    return answer


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



