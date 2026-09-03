chamados = [
    {
        "id": 1,
        "titulo": "Sem acesso ao sistema interno",
        "prioridade": "alta",
        "situacao": "aberto",
        "categoria": "acesso"
    },
    {
        "id": 2,
        "titulo": "Impressora sem conexão",
        "prioridade": "média",
        "situacao": "em atendimento",
        "categoria": "hardware"
    },
    {
        "id": 3,
        "titulo": "Internet instável",
        "prioridade": "alta",
        "situacao": "aberto",
        "categoria": "rede"
    },
    {
        "id": 4,
        "titulo": "Computador não liga",
        "prioridade": "alta",
        "situacao": "fechado",
        "categoria": "hardware"
    },
    {
        "id": 5,
        "titulo": "Problema com senha",
        "prioridade": "média",
        "situacao": "aberto",
        "categoria": "acesso"
    }
]

print("=" * 40)
print("TODOS OS CHAMADOS")
print("=" * 40)

for chamado in chamados:
    print(f"ID: {chamado['id']}")
    print(f"Título: {chamado['titulo']}")
    print(f"Prioridade: {chamado['prioridade']}")
    print(f"Situação: {chamado['situacao']}")
    print(f"Categoria: {chamado['categoria']}")
    print("-" * 40)

situacao_desejada = "aberto"
encontrou_chamado = False

print()
print("=" * 40)
print(f"CHAMADOS COM SITUAÇÃO: {situacao_desejada}")
print("=" * 40)

for chamado in chamados:
    if chamado["situacao"] == situacao_desejada:
        print(f"ID: {chamado['id']}")
        print(f"Título: {chamado['titulo']}")
        print(f"Prioridade: {chamado['prioridade']}")
        print(f"Categoria: {chamado['categoria']}")
        print("-" * 40)

        encontrou_chamado = True

if not encontrou_chamado:
    print("Nenhum chamado encontrado para a situação informada.")

situacao_desejada = "cancelado"
encontrou_chamado = False

print()
print("=" * 40)
print(f"TESTE DE SITUAÇÃO: {situacao_desejada}")
print("=" * 40)

for chamado in chamados:
    if chamado["situacao"] == situacao_desejada:
        print(f"ID: {chamado['id']}")
        print(f"Título: {chamado['titulo']}")

        encontrou_chamado = True

if not encontrou_chamado:
    print("Nenhum chamado encontrado para a situação informada.")

id_procurado = 3
nova_situacao = "fechado"
encontrou_chamado = False

print()
print("=" * 40)
print("ATUALIZAÇÃO DE CHAMADO")
print("=" * 40)

for chamado in chamados:
    if chamado["id"] == id_procurado:
        chamado["situacao"] = nova_situacao

        print("Situação atualizada com sucesso.")
        print(f"ID: {chamado['id']}")
        print(f"Nova situação: {chamado['situacao']}")

        encontrou_chamado = True

        break

if not encontrou_chamado:
    print("Chamado não encontrado.")

id_procurado = 99
encontrou_chamado = False

print()
print("=" * 40)
print("TESTE DE ID INEXISTENTE")
print("=" * 40)

for chamado in chamados:
    if chamado["id"] == id_procurado:
        chamado["situacao"] = "fechado"

        encontrou_chamado = True

        break

if not encontrou_chamado:
    print("Chamado não encontrado.")

categorias = set()

for chamado in chamados:
    categorias.add(chamado["categoria"])

print()
print("=" * 40)
print("CATEGORIAS EXISTENTES")
print("=" * 40)

for categoria in categorias:
    print(categoria)

print()
print("=" * 40)
print("PROGRAMA FINALIZADO")
print("=" * 40)