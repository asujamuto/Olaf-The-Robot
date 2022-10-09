from django.db import models

# Create your models here.

class Conversation(models.Model):
    user_message = models.CharField(max_length = 200)
    bot_message = models.CharField(max_length = 200)
    tag =  models.CharField(max_length = 100)
    date = models.DateTimeField(auto_now_add=True)
