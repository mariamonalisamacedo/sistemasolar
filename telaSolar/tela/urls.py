from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('cadastro/pf/', views.PessoaFisicaCreateView.as_view(), name='cadastro_pf'),
    path('cadastro/pj/', views.PessoaJuridicaCreateView.as_view(), name='cadastro_pj'),
]