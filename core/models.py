from django.db import models

class Livro(models.Model):
    titulo = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    isbn = models.CharField(max_length=13)
    preco = models.DecimalField(max_digits=10, decimal_places=2)
    cod_fornecedor = models.ForeignKey('Fornecedor', on_delete=models.CASCADE)

class Fornecedor(models.Model):
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200)
    telefone = models.CharField(max_length=15)
    cnpj = models.CharField(max_length=14)

