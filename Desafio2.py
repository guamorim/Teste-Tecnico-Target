import json

# Carrega o estoque
with open("estoque.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

estoque = dados["estoque"]

# Tenta carregar o histórico de movimentações
try:
    with open("movimentacoes.json", "r", encoding="utf-8") as arquivo:
        dados_movimentacoes = json.load(arquivo)
        movimentacoes = dados_movimentacoes["movimentacoes"]

except (FileNotFoundError, json.JSONDecodeError):
    movimentacoes = []


while True:
    print("\n=== MOVIMENTAÇÃO DE ESTOQUE ===")

    codigo = int(input("Código do produto: "))

    produto_encontrado = None

    for produto in estoque:
        if produto["codigoProduto"] == codigo:
            produto_encontrado = produto
            break

    if produto_encontrado is None:
        print("Produto não encontrado.")
    else:
        print(f"Produto: {produto_encontrado['descricaoProduto']}")
        print(f"Estoque atual: {produto_encontrado['estoque']}")

        tipo = input("Digite E para entrada ou S para saída: ").upper()
        quantidade = int(input("Quantidade: "))
        descricao = input("Descrição da movimentação: ")

        if quantidade <= 0:
            print("A quantidade deve ser maior que zero.")

        elif tipo == "E":
            produto_encontrado["estoque"] += quantidade

            id_movimentacao = len(movimentacoes) + 1

            movimentacoes.append({
                "id": id_movimentacao,
                "codigoProduto": codigo,
                "tipo": "Entrada",
                "descricao": descricao,
                "quantidade": quantidade,
                "estoqueFinal": produto_encontrado["estoque"]
            })

            print("Entrada realizada com sucesso.")
            print(f"Estoque final: {produto_encontrado['estoque']}")

        elif tipo == "S":
            if quantidade > produto_encontrado["estoque"]:
                print("Estoque insuficiente.")
            else:
                produto_encontrado["estoque"] -= quantidade

                id_movimentacao = len(movimentacoes) + 1

                movimentacoes.append({
                    "id": id_movimentacao,
                    "codigoProduto": codigo,
                    "tipo": "Saída",
                    "descricao": descricao,
                    "quantidade": quantidade,
                    "estoqueFinal": produto_encontrado["estoque"]
                })

                print("Saída realizada com sucesso.")
                print(f"Estoque final: {produto_encontrado['estoque']}")

        else:
            print("Tipo de movimentação inválido.")

        # Salva o estoque atualizado
        with open("estoque.json", "w", encoding="utf-8") as arquivo:
            json.dump(dados, arquivo, ensure_ascii=False, indent=4)

        # Salva o histórico
        with open("movimentacoes.json", "w", encoding="utf-8") as arquivo:
            json.dump(
                {"movimentacoes": movimentacoes},
                arquivo,
                ensure_ascii=False,
                indent=4
            )

    continuar = input("\nDeseja fazer outra movimentação? (S/N): ").upper()

    if continuar != "S":
        break