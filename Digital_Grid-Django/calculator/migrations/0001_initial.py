# Generated by Django 5.0 on 2024-04-19 18:02

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DiscountRules',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('consumer_type', models.CharField(choices=[('R', 'Residencial'), ('C', 'Comercial'), ('I', 'Industrial')], max_length=1, verbose_name='Tipo do Consumidor')),
                ('consumption_range', models.CharField(choices=[('B', '< 10.000 kWh'), ('M', '>= 10.000 kWh e <= 20.000 kWh'), ('A', '> 20.000 kWh')], max_length=1, verbose_name='Faixa de Consumo')),
                ('cover_value', models.CharField(choices=[('B', '< 10.000 kWh'), ('M', '>= 10.000 kWh e <= 20.000 kWh'), ('A', '> 20.000 kWh')], max_length=1, verbose_name='Valor de Cobertura')),
                ('discount_value', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Valor de Desconto')),
            ],
        ),
        migrations.CreateModel(
            name='Consumer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=128, verbose_name='Nome do Consumidor')),
                ('document', models.CharField(max_length=14, unique=True, verbose_name='Documento(CPF/CNPJ)')),
                ('zip_code', models.CharField(blank=True, max_length=8, null=True, verbose_name='CEP')),
                ('city', models.CharField(max_length=128, verbose_name='Cidade')),
                ('state', models.CharField(max_length=128, verbose_name='Estado')),
                ('consumption', models.IntegerField(blank=True, null=True, verbose_name='Consumo(kWh)')),
                ('distributor_tax', models.FloatField(blank=True, null=True, verbose_name='Tarifa da Distribuidora')),
                ('discount_rule', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calculator.discountrules')),
            ],
        ),
    ]
