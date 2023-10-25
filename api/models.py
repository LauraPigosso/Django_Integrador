from django.db import models

class Cliente(models.Model):
    nome = models.CharField(max_length=225)
    cidade = models.CharField(max_length=225)