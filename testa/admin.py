from django.contrib import admin, Question, Choice
from .models import Notes

# Register your models here.
admin.site.register(Question)
admin.site.register(Notes)
admin.site.register(Choice)
