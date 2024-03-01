from django.contrib import admin
from .models import Question, Notes, Choice

# Register your models here.
admin.site.register(Question)
admin.site.register(Notes)
admin.site.register(Choice)