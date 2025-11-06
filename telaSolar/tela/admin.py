from django.contrib import admin
from .models import PessoaFisica, PessoaJuridica

@admin.register(PessoaFisica)
class PessoaFisicaAdmin(admin.ModelAdmin):
    list_display = ('cpf', 'nome_fantasia', 'email', 'telefone_principal', 'cidade', 'estado')
    search_fields = ('cpf', 'nome_fantasia', 'email')
    list_filter = ('estado', 'cidade')

@admin.register(PessoaJuridica)
class PessoaJuridicaAdmin(admin.ModelAdmin):
    list_display = ('cnpj', 'razao_social', 'email', 'telefone_principal', 'cidade', 'estado')
    search_fields = ('cnpj', 'razao_social', 'email')
    list_filter = ('estado', 'cidade')
