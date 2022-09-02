from django.shortcuts import render, redirect

from django.http import HttpResponse


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
    context = {
        'username': "Jakub",
        'notes' : notesList,
    }
    return render(request, template_name='notes/notes.html', context=context)

def note(request, note_id):
    noteObject = None
    for note in notesList:
        if note['slug'] == note_id:
            noteObject = note
    
    context = {
        'title': noteObject['title'],
        'note': noteObject
    }
    return render(request, template_name="notes/single-note.html", context=context)


# Create your views here.
