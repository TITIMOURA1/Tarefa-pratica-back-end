from django.contrib import admin

from .models import Categoria, Tarefa


@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    search_fields = ("nome",)


@admin.register(Tarefa)
class TarefaAdmin(admin.ModelAdmin):
    list_display = ("titulo", "categoria", "prioridade", "data_prevista", "situacao")
    list_filter = ("categoria", "prioridade", "situacao")
    search_fields = ("titulo", "descricao")
