# models.py

from django.db import models
from django.contrib.auth.models import User  # Import User model if needed

class Note(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    # Additional fields (optional)
    tags = models.ManyToManyField('Tag', related_name='notes')
    categories = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, related_name='notes')
    # Collaborators (if needed)
    collaborators = models.ManyToManyField(User, related_name='collaborator_notes')

    def __str__(self):
        return self.title
