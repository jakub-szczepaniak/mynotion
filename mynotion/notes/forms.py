from django.forms import ModelForm, formset_factory
from .models import Note, Block

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['title']

class BlockForm(ModelForm):
    class Meta:
        model = Block
        fields = ['content', 'tag']


 