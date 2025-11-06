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
