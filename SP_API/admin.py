from django.contrib import admin

from .models import InvestigadorPrincipal, Pesquisa, EntradaFinanceira, EquipeDeApoio, SaidaFinanceira, Paciente

# Register your models here.

admin.site.register(Pesquisa)
admin.site.register(EntradaFinanceira)
admin.site.register(SaidaFinanceira)
admin.site.register(EquipeDeApoio)
admin.site.register(InvestigadorPrincipal)
admin.site.register(Paciente)
