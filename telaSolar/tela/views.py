from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .models import PessoaFisica, PessoaJuridica
from django.urls import reverse_lazy


def home(request):
    return render(request, 'tela/home.html')


class PessoaFisicaCreateView(CreateView):
    model = PessoaFisica
    template_name = 'tela/pessoa_fisica_form.html'
    fields = '__all__'
    success_url = reverse_lazy('home')


class PessoaJuridicaCreateView(CreateView):
    model = PessoaJuridica
    template_name = 'tela/pessoa_juridica_form.html'
    fields = '__all__'
    success_url = reverse_lazy('home')





def registrations_list(request):
    """Lista combinada de cadastros: Pessoa Fisica e Pessoa Juridica."""
    pf_qs = PessoaFisica.objects.all().values(
        'id', 'cpf', 'nome_fantasia', 'email', 'telefone_principal', 'cidade'
    )
    pj_qs = PessoaJuridica.objects.all().values(
        'id', 'cnpj', 'razao_social', 'email', 'telefone_principal', 'cidade'
    )

    items = []
    for p in pf_qs:
        items.append({
            'type': 'Pessoa Física',
            'identifier': p['cpf'],
            'name': p['nome_fantasia'] or '',
            'email': p['email'],
            'phone': p['telefone_principal'],
            'city': p['cidade'],
            'pk': p['id'],
        })
    for p in pj_qs:
        items.append({
            'type': 'Pessoa Jurídica',
            'identifier': p['cnpj'],
            'name': p['razao_social'],
            'email': p['email'],
            'phone': p['telefone_principal'],
            'city': p['cidade'],
            'pk': p['id'],
        })

    # opcional: ordenar por name
    items.sort(key=lambda x: (x['type'], x['name'] or x['identifier']))

    return render(request, 'tela/registrations_list.html', {'items': items})
