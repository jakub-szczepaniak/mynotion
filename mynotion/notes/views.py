from django.shortcuts import render, redirect

from django.http import HttpResponse
from .models import Note, Block

notesList = [
    {
        'slug': 'New-note',
        'title': 'Untitled',
        'content': ''
    },
    {
        'slug': 'Project-List',
        'title': 'Project List',
        'content': "Abnsss this is the project list"
    }
]

def notes(request):
    notes = Note.objects.all
    context = {
        'username': "Jakub",
        'notes' : notes,
    }
    return render(request, template_name='notes/notes.html', context=context)

def note(request, note_id):
    note = Note.objects.get(id=note_id)
    context = {
        'title': note.title,
        'note': note,
        'blocks': note.blocks.all()

    }
    return render(request, template_name="notes/single-note.html", context=context)


# Create your views here.
