# Generated by Django 2.1 on 2019-09-20 01:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SP_API', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pesquisa',
            name='data_termino',
            field=models.DateField(auto_now=True, verbose_name='Data de Término da Pesquisa'),
        ),
    ]
