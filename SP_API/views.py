from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
from SP_API.models import Pesquisa, InvestigadorPrincipal, EquipeDeApoio, EntradaFinanceira, SaidaFinanceira
from SP_API.serializers import PesquisaSerializer, InvestigadorPrincipalSerializer, EquipeDeApoioSerializer, \
    EntradaFinanceiraSerializer, SaidaFinanceiraSerializer, EntradaFinanceiraReadSerializer, \
    SaidaFinanceiraReadSerialzier


class PesquisaViewSet(viewsets.ModelViewSet):
    queryset = Pesquisa.objects.all()
    serializer_class = PesquisaSerializer


class InvestigadorViewSet(viewsets.ModelViewSet):
    queryset = InvestigadorPrincipal.objects.all()
    serializer_class = InvestigadorPrincipalSerializer


class EquipeDeApoioViewSet(viewsets.ModelViewSet):
    queryset = EquipeDeApoio.objects.all()
    serializer_class = EquipeDeApoioSerializer


class EntradaFinanceiraViewSet(viewsets.ModelViewSet):
    queryset = EntradaFinanceira.objects.all()
#    serializer_class = EntradaFinanceiraSerializer

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return EntradaFinanceiraReadSerializer
        return EntradaFinanceiraSerializer


class SaidaFinanceiraViewSet(viewsets.ModelViewSet):
    queryset = SaidaFinanceira.objects.all()
#    serializer_class = SaidaFinanceiraSerializer

    def get_serializer_class(self):
        if self.request.method in ['GET']:
            return SaidaFinanceiraReadSerialzier
        return SaidaFinanceiraSerializer


@csrf_exempt
def teste(request, *args, **kwargs):
    print(request.data)
    return "Aee"
