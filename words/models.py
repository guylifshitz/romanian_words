from django.db import models


class Word(models.Model):
    romanian = models.CharField(max_length=200)
    english = models.CharField(max_length=200)
    score = models.IntegerField()
    level = models.IntegerField()