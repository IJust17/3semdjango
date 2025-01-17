from django.db import models
from simple_history.models import HistoricalRecords


class Author(models.Model):
    name = models.CharField(max_length=100)
    history = HistoricalRecords()

    def __str__(self):
        return self.name


class File(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='files')
    name = models.CharField(max_length=255)
    file = models.FileField(upload_to='files/')
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)

    # демонстрация перезаписи порядка (reorder)
    sort_index = models.IntegerField(default=0)

    history = HistoricalRecords()

    def __str__(self):
        return f'File: {self.name} (Author: {self.author.name})'


class Comment(models.Model):
    file = models.ForeignKey(File, on_delete=models.CASCADE, related_name='comments')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    history = HistoricalRecords()

    def __str__(self):
        return f'Comment {self.id} for {self.file.name}'
