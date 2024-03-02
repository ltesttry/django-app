from django.contrib import admin
from .models import Notes, Question

# Register your models here.
admin.site.register(Question)
admin.site.register(Notes)
