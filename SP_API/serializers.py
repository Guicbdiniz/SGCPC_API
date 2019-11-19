from rest_framework import serializers
from SP_API.models import Pesquisa, InvestigadorPrincipal, EquipeDeApoio, EntradaFinanceira, SaidaFinanceira, Paciente


class InvestigadorPrincipalSerializer(serializers.ModelSerializer):
    class Meta:
        model = InvestigadorPrincipal
        fields = ('id', 'nome', 'email', 'telefone')


class EquipeDeApoioSerializer(serializers.ModelSerializer):
    class Meta:
        model = EquipeDeApoio
        fields = ('id', 'nome_da_coordenacao', 'email', 'telefone')


class PesquisaSerializer(serializers.ModelSerializer):
    equipe_de_apoio = EquipeDeApoioSerializer()
    investigador = InvestigadorPrincipalSerializer()

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

    def update(self, instance, validated_data):
        for data in validated_data:

            if data == "investigador":
                investigador = InvestigadorPrincipal.objects.get_or_create(**validated_data['investigador'])
                instance.investigador = investigador
            elif data == 'equipe_de_apoio':
                equipe = EquipeDeApoio.objects.get_or_create(**validated_data['equipe_de_apoio'])
                instance.equipe_de_apoio = equipe
            else:
                setattr(instance, data, validated_data[data])

        instance.save()
        return instance

# class PesquisaReadSerializer(PesquisaSerializer):
#    investigador = InvestigadorPrincipalSerializer(read_only=True)
#    equipe_de_apoio = EquipeDeApoioSerializer(read_only=True)


class EntradaFinanceiraSerializer(serializers.ModelSerializer):
    class Meta:
        model = EntradaFinanceira
        fields = '__all__'

    def create(self, validated_data):
        dados_da_pesquisa = validated_data.pop('pesquisa')
        entrada_financeira = EntradaFinanceira.objects.create(pesquisa=dados_da_pesquisa, **validated_data)

        return entrada_financeira

    def update(self, instance, validated_data):
        for data in validated_data:
            if data != 'pesquisa' and data != 'id':
                setattr(instance, data, validated_data[data])

        instance.save()
        return instance


class EntradaFinanceiraReadSerializer(EntradaFinanceiraSerializer):
    pesquisa = PesquisaSerializer(read_only=True)


class SaidaFinanceiraSerializer(serializers.ModelSerializer):
    class Meta:
        model = SaidaFinanceira
        fields = '__all__'

    def update(self, instance, validated_data):
        for data in validated_data:
            if data != 'pesquisa' and data != 'id':
                setattr(instance, data, validated_data[data])
            instance.save()
            return instance

#    def create(self, validated_data):
#        dados_da_pesquisa = validated_data.pop('pesquisa_id')
#        pesquisa = Pesquisa.objects.get(id=dados_da_pesquisa)
#        saida_financeira = SaidaFinanceira.objects.create(pesquisa=pesquisa, **validated_data)
#
#        return saida_financeira


class SaidaFinanceiraReadSerialzier(SaidaFinanceiraSerializer):
    pesquisa = PesquisaSerializer(read_only=True)


class PacienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paciente
        fields = '__all__'
