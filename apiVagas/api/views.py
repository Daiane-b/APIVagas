from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse

class VagaList(APIView):
    def post(self, request):
        try:
            serializer = VagaSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_RESQUEST)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def get(self, request):
        try:
            lista_vagas = Vaga.objects.all() # Obtemos a lista com todas as vagas cadastradas no banco de dados e salvamos na variável lista_vagas;
            serializer = VagaSerializer(lista_vagas, many=True) # Utilizando o VagaSerializer, mapeamos os dados das vagas obtidas do banco de dados para serem retornadas através da requisição;
            return Response(serializer.data)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
     status=status.HTTP_500_INTERNAL_SERVER_ERROR)

class VagaDetalhes(APIView):
    def get(self, resquest, pk):
        try:
            if pk == '0':
                return JsonResponse({'mensagem': "O id deve ser maior que zero"},
                                    status=status.HTTP_400_BAD_REQUEST)
            vaga = Vaga.objects.get(pk=pk)
            serializer = VagaSerializer(vaga)
            return Response(serializer.data)
        except Vaga.DoesNotExist:
            return JsonResponse({'mensagem': "A vaga não existe"},
                                status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({'mensagem':"Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def put(self, resquest, pk):
        try:
            if pk == "0":
                return JsonResponse({'mensagem':"O id deve ser maior que zero."},
                                    status=status.HTTP_400_BAD_REQUEST)
            vaga = Vaga.objects.get(pk=pk)
            serializer = VagaSerializer(vaga, data=resquest.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data)
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
        except Vaga.DoesNotExist:
            return JsonResponse({'mensagem':"A vaga não existe"},
                                status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    def delete(self, request, pk):
        try:
            if pk == "0":
                return JsonResponse({'mensagem':"O id deve ser maior que zero."},
                                    status=status.HTTP_400_BAD_REQUEST)
            vaga = Vaga.objects.get(pk=pk)
            vaga.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        except Vaga.DoesNotExist:
            return JsonResponse({'mensagem':"A vaga não existe"},
                                status=status.HTTP_404_NOT_FOUND)
        except Exception:
            return JsonResponse({'mensagem': "Ocorreu um erro no servidor"},
                                status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Create your views here.
