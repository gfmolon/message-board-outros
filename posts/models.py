# posts/models.py
from django.db import models


class Post(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:50]


class Receita(models.Model):
    text = models.TextField()

    def __str__(self):
        return self.text[:50]


class Produto(models.Model):
    nome = models.CharField(max_length=100)
    descricao = models.TextField(blank=True)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    estoque = models.IntegerField()
    imagem_pequena = models.ImageField(
        upload_to="produtos/thumbs/", blank=True, null=True
    )
    imagem_grande = models.ImageField(
        upload_to="produtos/grandes/", blank=True, null=True
    )
    data_criacao = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome
