from rest_framework import serializers
from SP_API.models import Pesquisa, InvestigadorPrincipal, EquipeDeApoio


class InvestigadorPrincipalSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestigadorPrincipal
        fields = ('id', 'nome', 'email', 'telefone')


class EquipeDeApoioSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipeDeApoio
        fields = ('id', 'nome_da_coordenacao', 'email', 'telefone')


class PesquisaSerializer(serializers.ModelSerializer):
    investigador = InvestigadorPrincipalSerializer(required=True)
    equipe_de_apoio = EquipeDeApoioSerializer(required=True)

    class Meta:
        model = Pesquisa
        fields = '__all__'

    def create(self, validated_data):
        dados_do_investigador = validated_data.pop('investigador')
        dados_da_equipe_de_apoio = validated_data.pop('equipe_de_apoio')
        investigador = InvestigadorPrincipalSerializer.create(InvestigadorPrincipalSerializer(), dados_do_investigador)
        equipe = EquipeDeApoioSerializer.create(EquipeDeApoioSerializer(), dados_da_equipe_de_apoio)
        pesquisa = Pesquisa.objects.create(investigador=investigador, equipe_de_apoio=equipe, **validated_data)

        return pesquisa
