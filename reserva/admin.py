from django.contrib import admin
from reserva.models import Reserva, CategoriaPet

@admin.register(Reserva)
class ReservaAdmin(admin.ModelAdmin):
    list_display = ['nome', 'email', 'nome_pet', 'data_apenas', 'turno', 'categoria', 'petshop']
    search_fields = ['nome', 'email', 'nome_pet']

@admin.register(CategoriaPet)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nome']
    search_fields = ['nome']
