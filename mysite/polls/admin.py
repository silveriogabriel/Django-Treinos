from django.contrib import admin
from .models import Enquete

@admin.register(Enquete)
class SimulacoeAdmin(admin.ModelAdmin):
    list_display = ("jogada", "banca_inicial", "stopgain", "stoploss", "banca_atual", "green", "red", "primeira_entrada","rendimento","created")
    prepopulated_fields = {"slug": ("jogada",)}
