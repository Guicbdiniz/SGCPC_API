from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt
from SP_API.models import Pesquisa, InvestigadorPrincipal, EquipeDeApoio
from SP_API.serializers import PesquisaSerializer, InvestigadorPrincipalSerializer, EquipeDeApoioSerializer


class PesquisaViewSet(viewsets.ModelViewSet):
    queryset = Pesquisa.objects.all()
    serializer_class = PesquisaSerializer


class InvestigadorViewSet(viewsets.ModelViewSet):
    queryset = InvestigadorPrincipal.objects.all()
    serializer_class = InvestigadorPrincipalSerializer


class EquipeDeApoioViewSet(viewsets.ModelViewSet):
    queryset = EquipeDeApoio.objects.all()
    serializer_class = EquipeDeApoioSerializer


@csrf_exempt
def teste(request, *args, **kwargs):
    print(request.data)
    return "Aee"
