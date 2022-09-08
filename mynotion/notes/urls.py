from django.urls import path
from . import views

urlpatterns = [
    path('', views.notes, name='notes'),
    path('notes/<slug:note_id>', views.note, name='note'),
    path('create-note/', views.createNote, name='create-note'),
    path('update-note/<slug:note_id>', views.updateNote, name='update-note'),
]