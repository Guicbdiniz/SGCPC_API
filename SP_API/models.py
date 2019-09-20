from django.db import models


class InvestigadorPrincipal(models.Model):
    nome = models.CharField('Nome do Investigador', max_length=30, default="Fulano")
    email = models.CharField('Email do investigador', max_length=20, default="exemplo@gmai.com")
    telefone = models.IntegerField('Número de telefone do investigador')


class EquipeDeApoio(models.Model):
    nome_da_coordenacao = models.CharField('Nome da Coordenação', max_length=30, default='Exemplo')
    email = models.CharField('Email da Equipe de Apoio', max_length=20, default='exemplo@gmail.com')
    telefone = models.IntegerField('Número de telefone da Equipe de Apoio')


class Pesquisa(models.Model):
    TIPOS_POSSIVEIS_DE_PESQUISA = (
        ('CL', 'Clinica'),
        ('CI', 'Científica'),
    )
    STATUS_POSSIVEIS = (
        ('EA', 'Em Andamento'),
        ('CO', 'Concluída'),
        ('CA', 'Cancelado')
    )
    TIPOS_DE_VINCULO = (
        ('PT', 'Pesquisa de Centro Terceirizado'),
        ('PI', 'Pesquisa Institucional'),
        ('PA', 'Pesquisa Acadêmica')
    )
    tipo_de_pesquisa = models.CharField(
        'Tipo de Pequisa', max_length=2, default='CL', choices=TIPOS_POSSIVEIS_DE_PESQUISA)
    titulo = models.CharField('Título da Pesquisa', max_length=30, default='Exemplo')
    nome_fantasia = models.CharField('Nome Fantasia da Pesquisa', max_length=30, default='Exemplo')
    numero_de_contrato = models.IntegerField('Número de contrato da Pesquisa', default='123')
    numero_CAAE = models.IntegerField('Numero da Plataforma Brasil', default='123')
    patrocinadores = models.CharField('Patrocinadores da Pesquisa', max_length=30, default='Exemplo')
    setor_de_atuacao = models.CharField('Setor de atuação da Pesquisa', max_length=30, default='Exemplo')
    investigador = models.ForeignKey(InvestigadorPrincipal, on_delete=models.CASCADE, null=True)
    status = models.CharField('Status da Pesquisa', max_length=2, default='EA', choices=STATUS_POSSIVEIS)
    equipe_de_apoio = models.ForeignKey(EquipeDeApoio, on_delete=models.CASCADE, null=True)
    vinculo_institucional = models.CharField(
        'Vínculo Institucional da Pesquisa', max_length=2, choices=TIPOS_DE_VINCULO, default='PT')
    data_inicio = models.DateField('Data de Início da Pesquisa', auto_now=True)
    data_termino = models.DateField('Data de Término da Pesquisa', blank=True, null=True)
