from django.conf.urls import url
from .views import *

urlpatterns = [
    url(r'^vagas$', VagaList.as_view()), # Criamos a rota responsável por chamar os metodos definidos na classe VagaList.
    url(r'^vagas/(?P<pk>[0-9]+)$', VagaDetalhes.as_view()),
]