from django.db import models


class Documento(models.Model):
    tipo = models.CharField(max_length=50)
    numeto = models.IntegerField()
    descricao = models.CharField(max_length=150)

    def __str__(self):
        return self.tipo
