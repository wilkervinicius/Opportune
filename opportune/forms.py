from django.forms import ModelForm
from .models import Lead, LeadAcoes


class LeadForm(ModelForm):
    class Meta:
        model = Lead
        fields = ['cliente', 'telefone', 'email']



class LeadAcoesForm(ModelForm):
    class Meta:
        model = LeadAcoes
        fields = ['interesse', 'data_agenda','hora_agenda', 'termometro','observacao']
        exclude = ['created_at']





