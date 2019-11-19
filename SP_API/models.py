from django.db import models


class InvestigadorPrincipal(models.Model):
    nome = models.CharField('Nome do Investigador', max_length=50, default="Fulano")
    email = models.CharField('Email do investigador', max_length=50, default="exemplo@gmai.com")
    telefone = models.CharField('Número de telefone do investigador', max_length=50)


class EquipeDeApoio(models.Model):
    nome_da_coordenacao = models.CharField('Nome da Coordenação', max_length=50, default='Exemplo')
    email = models.CharField('Email da Equipe de Apoio', max_length=50, default='exemplo@gmail.com')
    telefone = models.CharField('Número de telefone da Equipe de Apoio', max_length=50)


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
    titulo = models.CharField('Título da Pesquisa', max_length=80, default='Exemplo')
    nome_fantasia = models.CharField('Nome Fantasia da Pesquisa', max_length=30, default='Exemplo')
    numero_de_contrato = models.IntegerField('Número de contrato da Pesquisa', default='123')
    numero_CAAE = models.CharField('Numero da Plataforma Brasil', max_length=50, default='123')
    patrocinadores = models.CharField('Patrocinadores da Pesquisa', max_length=50, default='Exemplo')
    setor_de_atuacao = models.CharField('Setor de atuação da Pesquisa', max_length=50, default='Exemplo')
    investigador = models.ForeignKey(InvestigadorPrincipal, on_delete=models.SET_NULL, null=True)
    status = models.CharField('Status da Pesquisa', max_length=2, default='EA', choices=STATUS_POSSIVEIS)
    equipe_de_apoio = models.ForeignKey(EquipeDeApoio, on_delete=models.SET_NULL, null=True)
    vinculo_institucional = models.CharField(
        'Vínculo Institucional da Pesquisa', max_length=2, choices=TIPOS_DE_VINCULO, default='PT')
    data_inicio = models.DateField('Data de Início da Pesquisa', auto_now=True)
    data_termino = models.DateField('Data de Término da Pesquisa', blank=True, null=True)

    def __str__(self):
        return self.titulo


class EntradaFinanceira(models.Model):
    STATUS_POSSIVEIS = (
        ('EM', 'Emitida'),
        ('SE', 'Solicitada e aguardando emissão'),
        ('CA', 'Cancelada')
    )
    pesquisa = models.ForeignKey(Pesquisa, on_delete=models.DO_NOTHING, null=True)
    numero_nota_fiscal = models.CharField('Número da nota fiscal', max_length=50, default=1)
    data = models.DateField('Data de entrada da nota', auto_now=True)
    descricao = models.CharField('Descrição da entrada financeira', max_length=50, default='Sem descrição')
    valor = models.FloatField('Valor da entrada financeira', default=0)
    status = models.CharField('Status da entrada financeira', choices=STATUS_POSSIVEIS, max_length=2, default='EM')


class SaidaFinanceira(models.Model):
    STATUS_POSSIVEIS = (
        ('EM', 'Emitida'),
        ('SE', 'Solicitada e aguardando emissão'),
        ('CA', 'Cancelada')
    )
    recebedor = models.CharField('Nome do recebedor', max_length=30, default='Nenhum recebedor cadastrado')
    pesquisa = models.ForeignKey(Pesquisa, on_delete=models.DO_NOTHING, null=True)
    numero_nota_fiscal = models.CharField('Número da nota fiscal', max_length=50, default=1)
    data = models.DateField('Data de saída da nota', auto_now=True)
    descricao = models.CharField('Descrição da saída financeira', max_length=50, default='Sem descrição')
    valor = models.FloatField('Valor da saída financeira', default=0)
    status = models.CharField('Status da saída financeira', choices=STATUS_POSSIVEIS, max_length=2, default='EM')


class Paciente(models.Model):
    nome = models.CharField('Nome do paciente', max_length=30, default='Sem nome disponível')
    cpf = models.BigIntegerField('Cpf do paciente', default='12345678909')
    telefone = models.CharField('Número de celular do paciente', max_length=20, default='31999999999')
    pesquisa = models.ForeignKey(Pesquisa, on_delete=models.DO_NOTHING, null=True)
