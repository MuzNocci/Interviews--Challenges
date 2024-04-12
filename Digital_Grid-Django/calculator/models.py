from django.db import models



class DiscountRules(models.Model):


    TYPE_CHOICES = (
        ("R","Residencial"),
        ("C","Comercial"),
        ("I","Industrial"),
    )

    RANGE_CHOICES = (
        ("B","< 10.000 kWh"),
        ("M",">= 10.000 kWh e <= 20.000 kWh"),
        ("A","> 20.000 kWh"),
    )

    COVER_CHOICES = (
        ("B","< 10.000 kWh"),
        ("M",">= 10.000 kWh e <= 20.000 kWh"),
        ("A","> 20.000 kWh"),
    )


    customer_type = models.CharField("Tipo do Consumidor", max_length=1, choices=TYPE_CHOICES)
    consumption_range = models.CharField("Faixa de Consumo", max_length=1, choices=RANGE_CHOICES)
    cover_value = models.CharField("Valor de Cobertura", max_length=1, choices=COVER_CHOICES)
    discount_value = models.DecimalField("Valor de Desconto", decimal_places=2, max_digits=10)



class Consumer(models.Model):


    name = models.CharField("Nome do Consumidor", max_length=128)
    document = models.CharField("Documento(CPF/CNPJ)", max_length=14, unique=True)
    zip_code = models.CharField("CEP", max_length=8, null=True, blank=True)
    city = models.CharField("Cidade", max_length=128)
    state = models.CharField("Estado", max_length=128)
    consumption = models.IntegerField("Consumo(kWh)", blank=True, null=True)
    distributor_tax = models.FloatField("Tarifa da Distribuidora", blank=True, null=True)
    discount_rule = models.ForeignKey(DiscountRules, on_delete=models.CASCADE)
    #  create the foreign key for discount rule model here



# TODO: Create the model DiscountRules below
"""Fields:
-> Consumer type  
-> Consumption range
-> Cover value
-> Discount value
The first three fields should be a select with the values provided in the table
defined in the readme of the repository. Discount should be numerical
"""

# TODO: You must populate the consumer table with the data provided in the file consumers.xlsx
#  and associate each one with the correct discount rule
