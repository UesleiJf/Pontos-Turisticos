from rest_framework.viewsets import ModelViewSet
from atracoes.models import Atracao
from .serializers import DocIdentificacao


class DocIdentificacaoViewSet(ModelViewSet):
    queryset = Atracao.objects.all()
    serializer_class = DocIdentificacao

    filter_fields = ('tipo', 'nome', 'numero')