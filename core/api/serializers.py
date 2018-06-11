from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from DocIdentificacao.api.serializers import DocIdentificacaoSerializer
from DocIdentificacao.models import DocIdentificacao
from core.models import PontoTuristico, Atracao
from atracoes.api.serializers import AtracaoSerializer
from endereco.api.serializers import EnderecoSerializer
from comentarios.api.serializers import ComentarioSerializer
from avaliacoes.api.serializers import AvaliacaoSerializer
from endereco.models import Endereco


class PontoTuristicoSerializer(ModelSerializer):
    atracoes = AtracaoSerializer(many=True)
    endereco = EnderecoSerializer()
    comentario = ComentarioSerializer(many=True)
    avaliacoes = AvaliacaoSerializer(many=True)
    doc_identificacao = DocIdentificacaoSerializer()


    descricao_completa = SerializerMethodField()

    class Meta:
        model = PontoTuristico
        fields = ('id', 'nome', 'descricao', 'aprovado', 'foto',
                  'atracoes', 'comentario', 'avaliacoes', 'endereco', 'descricao_completa', 'descricao_completa2',
                  'doc_identificacao'
        )
        read_only_fileds = ('comentarios', 'avaliacoes')

    def cria_atracoes(self, atracoes, ponto):
        for atracao in atracoes:
            at = Atracao.objects.create(**atracao)
            ponto.atracoes.add(at)

    def create(self, validated_data):
        atracoes = validated_data['atracoes']
        del validated_data['atracoes']

        endereco = validated_data['endereco']
        del validated_data['endereco']

        doc = validated_data['doc_identificacao']
        del validated_data['doc_identificacao']
        doci = DocIdentificacao.objects.create(**doc)

        ponto = PontoTuristico.objects.create(**validated_data)
        self.cria_atracoes(atracoes, ponto)

        end = Endereco.objects.create(**endereco)
        ponto.endereco = end
        ponto.doc_identificacao = doci

        ponto.save()

        return ponto

    def get_descricao_completa(self, obj):
        return '%s - %s' % (obj.nome, obj.descricao)