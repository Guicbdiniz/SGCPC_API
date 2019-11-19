from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import inch, cm, mm
from reportlab.pdfgen.canvas import Canvas
from SP_API.models import Pesquisa


def adiciona_cabecalho_pdf(modelador_paginas):
    url_logo_hospistal = '/home/diniz/PUC/2019_2/TiS 3/SGCPC_API/IMGs/thumbnail_VERSAO-COR-01-Versao-padrao.jpeg'
    url_logo_puc = '/home/diniz/PUC/2019_2/TiS 3/SGCPC_API/IMGs/Logo-PUC-Minas.jpeg'
    modelador_paginas.drawImage(image=url_logo_hospistal, x=0, y=26 * cm, width=184, height=80)
    modelador_paginas.drawImage(image=url_logo_puc, x=16 * cm, y=26 * cm, width=130, height=100)
    modelador_paginas.saveState()
    modelador_paginas.setFont('Helvetica', size=42)
    modelador_paginas.drawString(text='Relatório de Pesquisas', x=3 * cm, y=24 * cm)
    modelador_paginas.restoreState()


def cria_pagina_pesquisa(modelador_paginas: Canvas, pesquisa: Pesquisa, numero_da_pesquisa: int):

    adiciona_cabecalho_pdf(modelador_paginas)

    modelador_paginas.setFont('Helvetica', 30)
    modelador_paginas.drawString(x=7.5 * cm, y=22 * cm, text='Pesquisa ' + str(numero_da_pesquisa))
    modelador_paginas.setFont('Helvetica', 20)
    modelador_paginas.drawString(x=2 * cm, y=20 * cm, text='Título: ' + pesquisa.titulo)
    modelador_paginas.drawString(x=2 * cm, y=18 * cm, text='Código: ' + str(pesquisa.id))
    modelador_paginas.drawString(x=2 * cm, y=16 * cm, text='Tipo de Pesquisa: ' + pesquisa.tipo_de_pesquisa)
    modelador_paginas.drawString(x=2 * cm, y=14 * cm, text='Investigador Principal: ' + pesquisa.investigador.nome)

    modelador_paginas.showPage()
