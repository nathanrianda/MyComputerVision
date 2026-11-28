from django.db import models

class SimpleComments(models.Model):
    nama = models.CharField(max_length=100)
    komentar = models.TextField()