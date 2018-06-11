from rest_framework.serializers import ModelSerializer
from DocIdentificacao.models import DocIdentificacao


class DocIdentificacaoSerializer(ModelSerializer):
    class Meta:
        model = DocIdentificacao
        fields = ['tipo', 'nome', 'numero',]