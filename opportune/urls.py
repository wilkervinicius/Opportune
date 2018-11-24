from django.urls import path

from . import views


app_name = 'opportune'

urlpatterns = [
    path('hello/', views.hello),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('geolocalizacao/', views.geolocalizacao, name = 'geolocalizacao'),
    path('list_lead_pendentes/', views.list_pendentes_lead, name="list_lead_pendentes"),
    path('list_lead_agendadas/', views.list_lead_agendadas, name="list_lead_agendadas"),
    path('list_lead_novos/', views.list_novo_lead, name = "list_lead_novos"),
    path('list_lead_hoje/', views.leads_hoje, name = "leads_hoje"),
    path('list_lead_semana/', views.leads_semana, name = "leads_semana"),
    path('list_lead_mes/', views.leads_mes, name = "leads_mes"),
    path('new_lead/', views.new_lead, name = "new_lead"),
    path('<int:lead_id>/new_acoes/', views.lead_acoes, name="lead_acoes"),
    path('<int:lead_id>/list_historico_lead/',views.list_historico_lead, name = 'list_historico_lead')


]