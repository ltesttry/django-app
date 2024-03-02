import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

#notes
#user

class Notes(models.Model):
    note = models.CharField(max_length=500)
    date = models.DateField()


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)