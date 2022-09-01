from django.shortcuts import render

from django.http import HttpResponse

def notes(request, note=''):
    status_code = 200
    if note == '':
        note = 'New-note'
        status_code = 301
    value = HttpResponse('This is the main page for notes' + str(note))
    value.headers['Location'] = note
    value.status_code = status_code
    
    return value
# Create your views here.
