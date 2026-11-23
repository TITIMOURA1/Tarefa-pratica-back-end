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

## Aplicação Django: persistência de tarefas e categorias

A aplicação Django fica na pasta `django`. Os models `Categoria` e `Tarefa` são armazenados no SQLite configurado no projeto, e uma tarefa pertence a uma categoria. Para preparar o banco local e carregar os registros de exemplo:

```powershell
cd django
python manage.py migrate
python manage.py loaddata dados_exemplo
python manage.py runserver
```

O fixture cria as categorias **Estudos** e **Pessoal** e duas tarefas pendentes. Acesse `/tarefas/` para conferir a listagem ou `/admin/` para administrar os registros (crie um administrador com `python manage.py createsuperuser`).

Para validar a persistência e atualizar uma tarefa pelo ORM:

```python
from tarefas.models import Categoria, Tarefa

Categoria.objects.all()
Tarefa.objects.all()
Tarefa.objects.filter(situacao="PENDENTE")
Tarefa.objects.order_by("data_prevista")

tarefa = Tarefa.objects.filter(situacao="PENDENTE").first()
tarefa.situacao = "CONCLUIDA"
tarefa.save()
Tarefa.objects.filter(situacao="CONCLUIDA")
```

**Dificuldade e solução:** a listagem inicial mantinha tarefas fixas na view, então os dados não sobreviviam ao reinício do servidor. A view passou a consultar os models no SQLite, com a relação entre tarefa e categoria registrada por migração; o fixture permite recriar os registros de demonstração em um banco local.
