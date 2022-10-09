from django.db import models

# Create your models here.
"""
class Messages(models.Model):
    message = models.CharField(max_length=500)
    user = models.ForeignKey(User, on_delete=models.CASCADE)


class User_Messages(models.Model):
    user_message = models.CharField(max_length = 200)

    def __str__(self):
        return self.user_message
    
class Answers(models.Model):
    answers = models.ForeignKey(User_Messages, on_delete=models.CASCADE)
    text = models.CharField(max_length = 300)
    complete = models.BooleanField()

    def __str__(self):
        return self.text
"""