import re
from django.shortcuts import render, redirect

from django.forms.models import modelformset_factory
from django.http import HttpResponse
from .models import Note, Block
from .forms import NoteForm, BlockForm

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
    note_form = NoteForm(instance=note)
    blocks = note.blocks.all()
    BlockFormset = modelformset_factory(Block, BlockForm, extra=1)
    block_formset = BlockFormset(request.POST or None, queryset=blocks)
    if request.method == 'POST':
        note_form = NoteForm(request.POST, instance=note)
        block_formset = BlockFormset(request.POST, queryset=blocks)
        
        if all([note_form.is_valid(), block_formset.is_valid()]):
            note = note_form.save(commit=False)
            note.save()
            for form in block_formset:
                block = form.save(commit=False)
                if block.note is None:
                    block.note = note
                block.save()
            return redirect('notes')
    
    context = { 'form' : note_form,
                'formset': block_formset }
    
    return render(request, 'notes/note-form.html', context=context)

def deleteNote(request, note_id):
    note = Note.objects.get(id=note_id)
    if request.method == 'POST':
        note.delete()
        return redirect('notes')
    context={'object': note}
    return render(request, 'notes/delete.html', context=context)