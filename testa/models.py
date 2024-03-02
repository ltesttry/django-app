import datetime

from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

#notes
#user

class Notes(models.Model):
    note = models.CharField(max_length=500)
    date = models.DateField()
    test1 = models.CharField(max_length=500, default="")


class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField()