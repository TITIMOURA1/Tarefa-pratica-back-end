from django.shortcuts import render

from .models import Categoria, Tarefa


def inicio(request):
    contexto = {
        "quantidade_categorias": Categoria.objects.count(),
        "quantidade_tarefas": Tarefa.objects.count(),
    }
    return render(request, "tarefas/inicio.html", contexto)


def lista_tarefas(request):
    contexto = {
        "tarefas": Tarefa.objects.select_related("categoria").all(),
        "categorias": Categoria.objects.all(),
    }
    return render(request, "tarefas/lista.html", contexto)
