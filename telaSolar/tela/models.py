from django.db import models

class PessoaFisica(models.Model):
    cpf = models.CharField(max_length=14, unique=True)
    nome_fantasia = models.CharField(max_length=150, blank=True, null=True)
    data_nascimento = models.DateField()
    rg = models.CharField(max_length=20, blank=True, null=True)

    email = models.EmailField()
    telefone_principal = models.CharField(max_length=15)
    telefone_secundario = models.CharField(max_length=15, blank=True, null=True)

    cep = models.CharField(max_length=9)
    logradouro = models.CharField(max_length=150)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=50, blank=True, null=True)
    bairro = models.CharField(max_length=80)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    pais = models.CharField(max_length=50)

    def __str__(self):
        return self.cpf

class PessoaJuridica(models.Model):
    cnpj = models.CharField(max_length=18, unique=True)
    razao_social = models.CharField(max_length=150)
    data_abertura = models.DateField()
    inscricao_estadual = models.CharField(max_length=20, blank=True, null=True)

    email = models.EmailField()
    telefone_principal = models.CharField(max_length=15)
    telefone_secundario = models.CharField(max_length=15, blank=True, null=True)
    site = models.URLField(blank=True, null=True)

    cep = models.CharField(max_length=9)
    logradouro = models.CharField(max_length=150)
    numero = models.CharField(max_length=10)
    complemento = models.CharField(max_length=50, blank=True, null=True)
    bairro = models.CharField(max_length=80)
    cidade = models.CharField(max_length=100)
    estado = models.CharField(max_length=2)
    pais = models.CharField(max_length=50)

    def __str__(self):
        return self.razao_social
