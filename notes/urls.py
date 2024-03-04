
from django.contrib import admin
from django.urls import path
 
from notes.views import *

urlpatterns = [
    path('', editor, name='editor'),
    path('delete_note/<int:noteid>/', delete_note, name='delete_note'),
]