from django.shortcuts import render, redirect

from django.http import HttpResponse

def notes(request, note=''):
    if note == '':
        return redirect(template_name='notes/note.html', note='New-note')
    else:
        return render(request, template_name='notes/note.html')
    
# Create your views here.
