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
    }
    return render(request, template_name='notes/notes.html', context=context)

def note(request, note):
    return render(request, template_name="notes/single-note.html")


# Create your views here.
