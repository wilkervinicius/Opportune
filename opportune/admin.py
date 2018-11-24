from django.contrib import admin

from .models import Regiao, Empresa, Termometro, Lead,LeadAcoes


admin.site.register(Termometro)
admin.site.register(Regiao)
admin.site.register(Empresa)
admin.site.register(Lead)
admin.site.register(LeadAcoes)