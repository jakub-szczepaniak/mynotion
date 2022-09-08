import re
from django.shortcuts import render, redirect

from django.http import HttpResponse
from .models import Note, Block
from .forms import NoteForm

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

def createNote(request):
    form = NoteForm()
    if request.method == 'POST':
        form = NoteForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('notes')
    context = { 'form': form}
    return render(request, 'notes/note-form.html', context=context)

def updateNote(request, note_id):
    note = Note.objects.get(id=note_id)
    form = NoteForm(instance=note)

    if request.method == 'POST':
        form = NoteForm(request.POST, instance=note)
        if form.is_valid:
            form.save()
            return redirect('notes')
    context = { 'form' : form }
    return render(request, 'notes/note-form.html', context=context)