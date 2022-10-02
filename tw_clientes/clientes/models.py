from django.db import models


class Cliente(models.Model):
    sexo_clientes = (
        ('F', 'Feminino'),
        ('M', 'Masculino'),
        ('N', 'Nenhuma das opções')
    )

    nome = models.CharField(max_length=100, null=False, blank=False)  # CharField é equivalente ao varchar do Mysql
    data_nascimento = models.DateField(null=False, blank=False)
    email = models.EmailField(null=False, blank=False)
    profissao = models.CharField(max_length=50, null=False, blank=False)
    sexo = models.CharField(max_length=1, choices=sexo_clientes, null=False, blank=False)

    def __str__(self):
        return self.nome
