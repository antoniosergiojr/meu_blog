from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Post(models.Model):
    titulo = models.CharField(max_length=255)
    resumo = models.CharField(max_length=255)
    conteudo = models.TextField()
    autor = models.ForeignKey(User, on_delete=models.PROTECT)
    data_criacao = models.DateField(auto_now_add=True)
