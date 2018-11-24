from django.shortcuts import render, HttpResponse, redirect , get_object_or_404
from django.conf import settings
from django.contrib.auth.decorators import login_required
#from django.utils.decorators import method_decorator
from .forms import LeadForm, LeadAcoesForm
from .models import Lead , LeadAcoes
from django.db.models import  Exists, OuterRef
from django.contrib import messages
import datetime


def hello(request):
    return HttpResponse('Hello Word!!!')

@login_required(login_url= settings.LOGIN_URL)
def dashboard(request):
   # objeto lead_acoes para associacao atraves de subquery com o modelo Lead
   lead_acoes = LeadAcoes.objects.filter(lead = OuterRef('pk'))
   # objeto lead_pendentes seleciona toas as leads que não tem ações ou não existe na tabela leadacoes
   lead_sem_acao = Lead.objects.annotate(lead_acoes_pendentes = ~Exists(lead_acoes),).filter(lead_acoes_pendentes = True).count()
   # objeto lead_novo seleciona todas as lead sem acões criadas no dia.

   today = datetime.date.today()



   lead_novo = Lead.objects.annotate(lead_acoes_novo = ~Exists(lead_acoes),
                                     ).filter(lead_acoes_novo = True).filter(created_at__contains= today).count()

   lead_hoje = Lead.objects.filter(data_agenda=today).count()
   lead_atrasada =  Lead.objects.filter(data_agenda__lt =today).count()

   lead_pendentes = lead_atrasada + lead_sem_acao

   lead_agendada = Lead.objects.filter(data_agenda__gte=today).count()

   lead_mes = Lead.objects.filter(data_agenda__year=today.strftime("%Y"), data_agenda__month=today.strftime("%m")).count()

   lead_semana =  Lead.objects.filter(data_agenda__week=today.strftime("%W")).count()

   template = 'index.html'
   contexto = {

       'lead_pendentes': lead_pendentes,
       'lead_novo': lead_novo,
       'leads_hoje': lead_hoje,
       'leads_agendada': lead_agendada,
       'leads_mes':lead_mes,
       'leads_semana':lead_semana

   }
   return render(request,template,contexto)

@login_required(login_url= settings.LOGIN_URL)
def geolocalizacao(request):
    return render(request, 'geolocalizacao.html')


@login_required(login_url= settings.LOGIN_URL)
def new_lead(request):
    form = LeadForm(request.POST, None)
    if form.is_valid():
        form.save()
        redirect('opportune:list_lead_novos')
        messages.success(request,'Lead cadastrada com sucesso')
    return render(request,'new_lead.html',{'form': form})


@login_required(login_url= settings.LOGIN_URL)
def list_novo_lead(request):
    start_date = datetime.date.today()

    lead_acoes = LeadAcoes.objects.filter(lead=OuterRef('pk'))
    leads_novos = Lead.objects.annotate(lead_acoes_novos=~Exists(lead_acoes),
                                      ).filter(lead_acoes_novos=True).filter(created_at__contains=start_date)

    return render(request,'list_lead_novos.html',{'leads_novos':leads_novos})

@login_required(login_url= settings.LOGIN_URL)
def list_pendentes_lead(request):
    today = datetime.date.today()

    lead_atrasada = Lead.objects.filter(data_agenda__lt=today).values('id','cliente')
    lead_acoes = LeadAcoes.objects.filter(lead=OuterRef('pk'))
    leads_sem_acao = Lead.objects.annotate(lead_acoes_pendentes=~Exists(lead_acoes),
                                      ).filter(lead_acoes_pendentes=True).values('id','cliente')


    leads_pendentes = lead_atrasada.union(leads_sem_acao)


    return render(request,'list_lead_pendentes.html',{'leads_pendentes':leads_pendentes})

@login_required(login_url= settings.LOGIN_URL)
def lead_acoes(request, lead_id):
    lead = get_object_or_404(Lead, pk = lead_id)

    form = LeadAcoesForm(request.POST or None)
    if form.is_valid():
        acao = form.save(commit=False)
        acao.lead = lead
        lead.data_agenda = acao.data_agenda
        lead.data_hora = acao.data_agenda
        lead.termometro = acao.termometro
        lead.save()
        acao.save()
        redirect('opportune:list_lead_agendadas')
        messages.success(request, 'Lead cadastrada com sucesso')
    template = 'new_acao.html'
    context = {
        'lead': lead,
        'form': form,

    }
    return render(request, template, context)

@login_required(login_url= settings.LOGIN_URL)
def leads_hoje(request):
    today = datetime.date.today()
    qs = Lead.objects.filter(data_agenda = today)


    template = 'list_lead_hoje.html'
    contexto = {

        'leads_hoje':qs

    }

    return render(request, template,contexto)

@login_required(login_url= settings.LOGIN_URL)
def leads_semana(request):
    today = datetime.date.today()
    lead_semana = Lead.objects.filter(data_agenda__week=today.strftime("%W"))


    template = 'list_lead_semana.html'
    contexto = {

        'leads_semana':lead_semana

    }

    return render(request, template, contexto)


@login_required(login_url= settings.LOGIN_URL)
def leads_mes(request):
    today = datetime.date.today()

    lead_mes = Lead.objects.filter(data_agenda__year = today.strftime("%Y"), data_agenda__month = today.strftime("%m") )


    template = 'list_lead_mes.html'
    contexto = {

        'leads_mes':lead_mes

    }

    return render(request, template,contexto)

@login_required(login_url= settings.LOGIN_URL)
def list_lead_agendadas(request):

    today = datetime.date.today()
    qs = Lead.objects.filter(data_agenda__gte = today)


    template = 'list_lead_agendadas.html'
    contexto = {

        'leads_agendadas':qs

    }

    return render(request, template,contexto)


@login_required(login_url= settings.LOGIN_URL)
def list_historico_lead(request, lead_id):
    lead = get_object_or_404(Lead, pk=lead_id)

    acoes_lead = LeadAcoes.objects.filter(lead_id = lead).order_by('-created_at')

    template = 'lead_historico.html'

    context = {

        'lead': lead,
        'acoes_lead': acoes_lead
    }


    return render(request,template,context)

