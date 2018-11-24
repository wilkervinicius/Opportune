from django.db import models
from django.utils import timezone


# Create your models here.


class Regiao(models.Model):
    nome = models.CharField('Nome', max_length=50)
    cod_regiao_erp = models.IntegerField()
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = "Região"
        verbose_name_plural = "Regiões"

    def __str__(self):
        return self.nome


class Empresa(models.Model):
    nome = models.CharField('Nome', max_length=50)
    cod_empresa_erp = models.IntegerField('Codigo Empresa ERP', null=True)
    regiao_id = models.ForeignKey(Regiao, on_delete=models.PROTECT)
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)

    class Meta:
        verbose_name = "Empresa"
        verbose_name_plural = "Empresas"

    def __str__(self):
        return self.nome



class Termometro(models.Model):
    descricao = models.CharField('Descrição', max_length=30)

    class Meta:
        verbose_name = "Termômetro"
        verbose_name_plural = "Termômetros"

    def __str__(self):
        return self.descricao


class Lead (models.Model):
    STATUS_CHOICE = (
        ('A', 'Aberto'),
        ('E', 'Encerrado'),
        ('D','Descartado')
    )

    cliente = models.CharField('Cliente', max_length=50)
    telefone = models.CharField('Telefone', max_length=11)
    email = models.EmailField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICE, default='A')
    created_at = models.DateTimeField('Criado em', auto_now_add=True)
    updated_at = models.DateTimeField('Atualizado em', auto_now=True)
 #   vendedor = models.ForeignKey(Vendedor,on_delete=models.PROTECT)
 #   lider = models.ForeignKey(Lider, on_delete=models.PROTECT)
    termometro = models.ForeignKey(Termometro, on_delete=models.PROTECT, default=1)
    data_agenda = models.DateField('Data Agendamento',blank=True, null=True)
    hora_agenda = models.TimeField('Hora Agendamento',blank=True, null=True)


    def sucesso(self):

        if self.status == 'A':
            self.status = 'E'
            self.save()

    def get_absolute_url(self):
        return ('opportune:new_lead')

    class Meta:
        verbose_name = 'Lead'
        verbose_name_plural = 'Leads'


    def __str__(self):
        return self.cliente



class LeadAcoes(models.Model):
    INTERESSE_CHOICE = (
        ('N', 'Novos'),
        ('U', 'Seminovos'),
        ('C', 'Consorcio'),
        ('T', 'Tele-Pecas'),
        ('S', 'Seguros'),
        ('A', 'Acessorios')
    )

    lead = models.ForeignKey(Lead, verbose_name='Lead',on_delete=models.CASCADE,
                             related_name='lead_acoes',null=True, default=1)
    interesse = models.CharField('Interesse',max_length=1, choices=INTERESSE_CHOICE, blank=True, null=True)
    created_at = models.DateTimeField('Criado em',  auto_now_add=True)
    data_agenda = models.DateField('Data Contato', blank=True, null=True)
    hora_agenda = models.TimeField('Hora Contato',blank=True, null=True)
    termometro = models.ForeignKey(Termometro, verbose_name='Termometro', on_delete=models.CASCADE, blank=True, null=True,
                                   related_name='lead_acoes', default=1)
    observacao = models.TextField('Observação',blank=True, null=True)

    class Meta:
        verbose_name = 'Lead Ação'
        verbose_name_plural = 'Leads Ações'



    def __str__(self):
        return  self.observacao

