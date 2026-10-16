from django.db import models


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    marca = models.CharField(max_length=50)
    preco = models.DecimalField(max_digits=8, decimal_places=2)
    estoque = models.IntegerField(default=0)
    descricao = models.CharField(max_length=500, blank=True, null=True)

    def __str__(self):
        return f"{self.marca} - {self.nome} - R$ {self.preco}"