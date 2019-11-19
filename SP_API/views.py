from reportlab.graphics.shapes import Image
from rest_framework import viewsets
from django.views.decorators.csrf import csrf_exempt

from SP_API.funcoes import cria_pagina_pesquisa
from SP_API.models import Pesquisa, InvestigadorPrincipal, EquipeDeApoio, EntradaFinanceira, SaidaFinanceira, Paciente
from SP_API.serializers import PesquisaSerializer, InvestigadorPrincipalSerializer, EquipeDeApoioSerializer, \
    EntradaFinanceiraSerializer, SaidaFinanceiraSerializer, EntradaFinanceiraReadSerializer, \
    SaidaFinanceiraReadSerialzier, PacienteSerializer
import io
from django.http import FileResponse
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch, cm, mm


class PacienteViewSet(viewsets.ModelViewSet):
    queryset = Paciente.objects.all()
    serializer_class = PacienteSerializer


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


def gerar_relatorio_de_pesquisa(request):

    buffer = io.BytesIO()
    modelador_paginas = canvas.Canvas(buffer, pagesize=A4)
    modelador_paginas.setTitle('Relatório de Pesquisas - Hospital São Francisco')

    pesquisas_cadastradas = Pesquisa.objects.all()

    contador_de_pesquisas = 1

    for pesquisa in pesquisas_cadastradas:
        cria_pagina_pesquisa(modelador_paginas, pesquisa, contador_de_pesquisas)
        contador_de_pesquisas += 1

    modelador_paginas.save()

    buffer.seek(0)

    return FileResponse(buffer, as_attachment=False, filename='relatório.pdf')
