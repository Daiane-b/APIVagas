from rest_framework import serializers
from .models import *

##Criamos a classe VagaSerializer responsável por mapear a entidade Vaga do projeto
class VagaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaga #Definimos que o model a ser utilizado pela classe VagaSerializer é o model de Vaga, definido no arquivo models.py
        fields = ["id", "titulo", "descricao", "salario",
                  "tipo_contrato", "status"] #Através do array fields,declaramos todos os atributos da vaga que serão retornados na requisição
