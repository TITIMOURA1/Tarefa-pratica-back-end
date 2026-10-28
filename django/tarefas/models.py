from django.db import models


class Categoria(models.Model):
    nome = models.CharField("nome", max_length=100, unique=True)

    class Meta:
        ordering = ["nome"]
        verbose_name = "categoria"
        verbose_name_plural = "categorias"

    def __str__(self):
        return self.nome


class Tarefa(models.Model):
    class Prioridade(models.TextChoices):
        BAIXA = "BAIXA", "Baixa"
        MEDIA = "MEDIA", "Média"
        ALTA = "ALTA", "Alta"

    class Situacao(models.TextChoices):
        PENDENTE = "PENDENTE", "Pendente"
        CONCLUIDA = "CONCLUIDA", "Concluída"

    titulo = models.CharField("título", max_length=200)
    descricao = models.TextField("descrição", blank=True)
    prioridade = models.CharField(
        "prioridade",
        max_length=10,
        choices=Prioridade.choices,
        default=Prioridade.MEDIA,
    )
    data_prevista = models.DateField("data prevista", blank=True, null=True)
    situacao = models.CharField(
        "situação",
        max_length=10,
        choices=Situacao.choices,
        default=Situacao.PENDENTE,
    )
    categoria = models.ForeignKey(
        Categoria,
        on_delete=models.PROTECT,
        related_name="tarefas",
        verbose_name="categoria",
    )

    class Meta:
        ordering = ["data_prevista", "titulo"]
        verbose_name = "tarefa"
        verbose_name_plural = "tarefas"

    def __str__(self):
        return self.titulo
