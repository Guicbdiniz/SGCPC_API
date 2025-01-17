# Generated by Django 2.1 on 2019-09-20 13:15

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SP_API', '0003_auto_20190920_0137'),
    ]

    operations = [
        migrations.AddField(
            model_name='equipedeapoio',
            name='email',
            field=models.CharField(default='exemplo@gmail.com', max_length=20, verbose_name='Email da Equipe de Apoio'),
        ),
        migrations.AddField(
            model_name='equipedeapoio',
            name='nome_da_coordenacao',
            field=models.CharField(default='Exemplo', max_length=30, verbose_name='Nome da Coordenação'),
        ),
        migrations.AddField(
            model_name='investigadorprincipal',
            name='email',
            field=models.CharField(default='exemplo@gmai.com', max_length=20, verbose_name='Email do investigador'),
        ),
        migrations.AddField(
            model_name='investigadorprincipal',
            name='nome',
            field=models.CharField(default='Fulano', max_length=30, verbose_name='Nome do Investigador'),
        ),
        migrations.AddField(
            model_name='pesquisa',
            name='data_inicio',
            field=models.DateField(auto_now=True, verbose_name='Data de Início da Pesquisa'),
        ),
        migrations.AddField(
            model_name='pesquisa',
            name='equipe_de_apoio',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='SP_API.EquipeDeApoio'),
        ),
        migrations.AddField(
            model_name='pesquisa',
            name='nome_fantasia',
            field=models.CharField(default='Exemplo', max_length=30, verbose_name='Nome Fantasia da Pesquisa'),
        ),
        migrations.AddField(
            model_name='pesquisa',
            name='numero_CAAE',
            field=models.IntegerField(default='123', verbose_name='Numero da Plataforma Brasil'),
        ),
        migrations.AddField(
            model_name='pesquisa',
            name='numero_de_contrato',
            field=models.IntegerField(default='123', verbose_name='Número de contrato da Pesquisa'),
        ),
        migrations.AddField(
            model_name='pesquisa',
            name='patrocinadores',
            field=models.CharField(default='Exemplo', max_length=30, verbose_name='Patrocinadores da Pesquisa'),
        ),
        migrations.AddField(
            model_name='pesquisa',
            name='setor_de_atuacao',
            field=models.CharField(default='Exemplo', max_length=30, verbose_name='Setor de atuação da Pesquisa'),
        ),
        migrations.AddField(
            model_name='pesquisa',
            name='status',
            field=models.CharField(choices=[('EA', 'Em Andamento'), ('CO', 'Concluída'), ('CA', 'Cancelado')], default='EA', max_length=2, verbose_name='Status da Pesquisa'),
        ),
        migrations.AddField(
            model_name='pesquisa',
            name='tipo_de_pesquisa',
            field=models.CharField(choices=[('CL', 'Clinica'), ('CI', 'Científica')], default='CL', max_length=2, verbose_name='Tipo de Pequisa'),
        ),
        migrations.AddField(
            model_name='pesquisa',
            name='titulo',
            field=models.CharField(default='Exemplo', max_length=30, verbose_name='Título da Pesquisa'),
        ),
        migrations.AddField(
            model_name='pesquisa',
            name='vinculo_institucional',
            field=models.CharField(choices=[('PT', 'Pesquisa de Centro Terceirizado'), ('PI', 'Pesquisa Institucional'), ('PA', 'Pesquisa Acadêmica')], default='PT', max_length=2, verbose_name='Vínculo Institucional da Pesquisa'),
        ),
        migrations.AlterField(
            model_name='pesquisa',
            name='investigador',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='SP_API.InvestigadorPrincipal'),
        ),
    ]
