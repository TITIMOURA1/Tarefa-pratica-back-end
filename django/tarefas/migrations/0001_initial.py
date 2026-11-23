from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Categoria",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("nome", models.CharField(max_length=100, unique=True, verbose_name="nome")),
            ],
            options={
                "verbose_name": "categoria",
                "verbose_name_plural": "categorias",
                "ordering": ["nome"],
            },
        ),
        migrations.CreateModel(
            name="Tarefa",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("titulo", models.CharField(max_length=200, verbose_name="título")),
                ("descricao", models.TextField(blank=True, verbose_name="descrição")),
                (
                    "prioridade",
                    models.CharField(
                        choices=[("BAIXA", "Baixa"), ("MEDIA", "Média"), ("ALTA", "Alta")],
                        default="MEDIA",
                        max_length=10,
                        verbose_name="prioridade",
                    ),
                ),
                (
                    "data_prevista",
                    models.DateField(blank=True, null=True, verbose_name="data prevista"),
                ),
                (
                    "situacao",
                    models.CharField(
                        choices=[("PENDENTE", "Pendente"), ("CONCLUIDA", "Concluída")],
                        default="PENDENTE",
                        max_length=10,
                        verbose_name="situação",
                    ),
                ),
                (
                    "categoria",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.PROTECT,
                        related_name="tarefas",
                        to="tarefas.categoria",
                        verbose_name="categoria",
                    ),
                ),
            ],
            options={
                "verbose_name": "tarefa",
                "verbose_name_plural": "tarefas",
                "ordering": ["data_prevista", "titulo"],
            },
        ),
    ]
