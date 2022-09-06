from django.db import models
import uuid

# Create your models here.
class Note(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    slug = models.SlugField(max_length=100)
    title = models.CharField(max_length=100)
    created = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return str(self.slug) + "-" + str(self.id)


class Block(models.Model):
    id = models.UUIDField(default=uuid.uuid4, unique=True, primary_key=True, editable=False)
    content = models.TextField(null=True, blank=True)
    note = models.ForeignKey(Note, on_delete=models.CASCADE, null=True, blank=True)
    tag = models.CharField(max_length=10,null=False, default="p", blank=False)

    def __str__(self):
        return str(self.tag) + " in note: " + self.note.title