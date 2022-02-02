from pyexpat import model
from django.db import models
from django.contrib.auth.models import User

class Logins(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    ip = models.CharField(max_length=50)
    data = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.user.username

class Enquete(models.Model):
    jogada = models.CharField(max_length=255, default='Esta é a jogada Nº: ')
    slug = models.SlugField(max_length=255, unique=True)
    banca_inicial = models.FloatField(default=0)
    stopgain = models.IntegerField(default=0)
    stoploss = models.IntegerField(default=0)
    banca_atual = models.FloatField(default=0)
    green = models.FloatField(default=0)
    red = models.FloatField(default=0)
    primeira_entrada = models.FloatField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.TimeField(auto_now_add=True)
    rendimento = models.FloatField(null=True)

    def __str__(self):
        return self.jogada.title()
