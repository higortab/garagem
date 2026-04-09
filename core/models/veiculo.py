from django.db import models


class Veiculo(models.Model):
    ano = models.IntegerField(blank=True, null=True, default=0)
    preco = models.DecimalField(max_digits=7, decimal_places=2, blank=True, null=True, default=0)
    modelo = models.ForeignKey('Modelo', on_delete=models.PROTECT)
    cor = models.ForeignKey('Cor', on_delete=models.PROTECT)
    acessorio = models.ManyToManyField('Acessorio', blank=True, related_name='veiculos')

    def __str__(self):
        return f'({self.id}) - {self.modelo.nome.upper()} - {self.cor.nome.upper()} - {self.ano}'