  
from django.shortcuts import render, redirect
from .models import Note
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User

@login_required()
def editor(request):
    noteid = int(request.GET.get('noteid', 0))
    notes = Note.objects.all()
    notes.user = request.user

    if request.method == 'POST':
        noteid = int(request.POST.get('noteid', 0))
        title = request.POST.get('title')
        content = request.POST.get('content', '')
 
        if noteid > 0:
            note = Note.objects.get(pk=noteid)
            note.title = title
            note.content = content
            note.save()
 
            return redirect('/?noteid=%i' % noteid)
        else:
            note = Note.objects.create(title=title, content=content)
 
            return redirect('/?noteid=%i' % note.id)
 
    if noteid > 0:
        note = Note.objects.get(pk=noteid)
    else:
        note = ''
 
    context = {
        'noteid': noteid,
        'notes': notes,
        'note': note,
    }
 
    return render(request, 'editor.html', context)
 
 
 
@login_required()
def delete_note(request, noteid):
    note = Note.objects.get(pk=noteid)
    note.delete()
 
    return redirect('/?noteid=0')