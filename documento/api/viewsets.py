from rest_framework.viewsets import ModelViewSet
from documento.models import Documento
from .serializers import DocumentoSerializer


class AtracaoViewSet(ModelViewSet):
    queryset = Documento.objects.all()
    serializer_class = DocumentoSerializer

    filter_fields = ('nome', 'descricao')