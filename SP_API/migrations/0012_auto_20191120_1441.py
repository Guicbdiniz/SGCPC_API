# Generated by Django 2.1 on 2019-11-20 14:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('SP_API', '0011_auto_20191120_1438'),
    ]

    operations = [
        migrations.AlterField(
            model_name='paciente',
            name='pesquisa',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='SP_API.Pesquisa'),
        ),
    ]
