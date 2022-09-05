from pyexpat import model
from django.db import models
import uuid

# Create your models here.
class Note(models.Model):
    id = models.UUIDField(uuid.uuid4, unique=True, primary_key=True, editable=False)
    slug = models.SlugField(max_length=100)
    title = models.CharField(max_length=100)
    content = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)
    