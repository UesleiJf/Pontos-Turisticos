from rest_framework.serializers import ModelSerializer
from documento.models import Documento


class DocumentoSerializer(ModelSerializer):
    class Meta:
        model = Documento
        fields = ('id', 'tipo', 'numero', 'descricao')
