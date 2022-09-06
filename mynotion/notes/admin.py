from django.contrib import admin

# Register your models here.
from .models import Note, Block

admin.site.register(Note)
admin.site.register(Block)