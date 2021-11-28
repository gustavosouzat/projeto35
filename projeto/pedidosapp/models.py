from django.db import models

# Create your models here.
class Pedido(models.Model):
    
    nome_pedido = models.CharField(max_length=200)
    telefone = models.CharField(max_length=200)
    desc_pedido = models.TextField
    valor_pedido = models.CharField(max_length=200)
    endere_pedido = models.CharField(max_length=200)


    def __str__(self):

        return self.nome_pedido