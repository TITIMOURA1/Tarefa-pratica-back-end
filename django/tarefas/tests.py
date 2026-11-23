from datetime import date

from django.contrib import admin
from django.test import TestCase

from .models import Categoria, Tarefa


class TarefaPersistenceTests(TestCase):
    def setUp(self):
        self.categoria = Categoria.objects.create(nome="Estudos")

    def test_categoria_and_tarefa_are_persisted_with_relationship(self):
        tarefa = Tarefa.objects.create(
            titulo="Revisar Django",
            descricao="Estudar models e migrações.",
            prioridade=Tarefa.Prioridade.ALTA,
            data_prevista=date(2026, 11, 5),
            categoria=self.categoria,
        )

        tarefa_salva = Tarefa.objects.get(pk=tarefa.pk)

        self.assertEqual(tarefa_salva.categoria, self.categoria)
        self.assertEqual(tarefa_salva.situacao, Tarefa.Situacao.PENDENTE)
        self.assertEqual(str(tarefa_salva), "Revisar Django")
        self.assertEqual(str(tarefa_salva.categoria), "Estudos")

    def test_pending_tasks_can_be_filtered_ordered_and_updated(self):
        tarefa = Tarefa.objects.create(
            titulo="Entregar atividade",
            data_prevista=date(2026, 11, 7),
            categoria=self.categoria,
        )

        pendentes = Tarefa.objects.filter(situacao="PENDENTE").order_by("data_prevista")
        self.assertEqual(list(pendentes), [tarefa])

        tarefa.situacao = Tarefa.Situacao.CONCLUIDA
        tarefa.save(update_fields=["situacao"])

        self.assertEqual(
            Tarefa.objects.get(pk=tarefa.pk).situacao,
            Tarefa.Situacao.CONCLUIDA,
        )
        self.assertFalse(Tarefa.objects.filter(situacao="PENDENTE").exists())

    def test_models_are_registered_in_admin(self):
        self.assertIn(Categoria, admin.site._registry)
        self.assertIn(Tarefa, admin.site._registry)


class ListaTarefasViewTests(TestCase):
    def test_list_view_shows_persisted_tasks_and_categories(self):
        categoria = Categoria.objects.create(nome="Pessoal")
        Tarefa.objects.create(titulo="Pagar conta", categoria=categoria)

        response = self.client.get("/tarefas/")

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Pagar conta")
        self.assertContains(response, "Pessoal")
        self.assertContains(response, "Pendente")
