import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

#notes
#user

class Notes(models.Model):
    note = models.CharField(max_length=500)

class Question(models.Model):
    question_text = models.CharField(max_length=200)



"""class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def __str__(self):
        return self.choice_text"""