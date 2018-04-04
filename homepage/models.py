from django.db import models

class Game(models.Model):
    title = models.CharField(max_length=255)
    platform = models.CharField(max_length=255)
