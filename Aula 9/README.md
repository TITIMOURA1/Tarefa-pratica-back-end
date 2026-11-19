# 📋 Sistema de Gerenciamento de Tarefas

Projeto desenvolvido para a disciplina de Laboratório de Programação Back-End.

## 👥 Integrantes

- Laryssa Meryene dos Santos Cardoso - RA: 202422933
- Nicholas Eduardo Pereira Sobrinho - RA: 202411284
- Thiago Moura de Araújo Aguiar - RA: 202422974

## 📁 Organização do Projeto

- `tarefa.py`: contém a classe Tarefa e seus métodos.
- `servicos.py`: contém as funções de cadastro, listagem e filtro.
- `main.py`: executa e demonstra o funcionamento do programa.

## ⚙️ Funcionalidades

O programa permite:

- Cadastrar tarefas.
- Listar tarefas.
- Filtrar tarefas pela situação.
- Marcar uma tarefa como concluída.

## ▶️ Como Executar

Abra o terminal na pasta do projeto e execute:

python main.py

## 🐍 Tecnologias

- Python

## 📌 Demonstração

O programa cria três tarefas de exemplo.

Uma das tarefas é marcada como concluída e, ao final, o programa mostra todas as tarefas e também as tarefas concluídas.

## Aula 9 — Persistindo tarefas e categorias com Django

A aplicação web da pasta `django/` persiste categorias e tarefas no SQLite local.
No diretório `django/`, execute:

```bash
python manage.py migrate
python manage.py runserver
```

Acesse `/admin/` para cadastrar categorias e tarefas. A listagem disponível em
`/tarefas/` consulta os registros persistidos, que continuam disponíveis após
reiniciar o servidor. A prioridade (`BAIXA`, `MEDIA`, `ALTA`) e a situação
(`PENDENTE`, `CONCLUIDA`) são escolhas padronizadas.

### Registro da atividade hands-on

Na adaptação, a listagem inicial continha tarefas fixas na view e não aceitava
objetos do banco. A view foi ajustada para consultar `Tarefa` e o template passou
a exibir os campos e as categorias relacionados.

Validação pelo shell do Django:

```python
from tarefas.models import Categoria, Tarefa
Tarefa.objects.filter(situacao="PENDENTE")
tarefa = Tarefa.objects.filter(situacao="PENDENTE").first()
tarefa.situacao = "CONCLUIDA"
tarefa.save()
Tarefa.objects.filter(pk=tarefa.pk, situacao="CONCLUIDA").exists()
```
