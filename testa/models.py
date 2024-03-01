
from django.db import models
from django.contrib.auth.models import User


#notes
#user

class Notes(models.Model):
    note = models.CharField(max_length=500)
