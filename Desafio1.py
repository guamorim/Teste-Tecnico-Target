import json

with open("vendas.json", "r", encoding="utf-8") as arquivo:
    dados = json.load(arquivo)

comissoes = {}

for venda in dados["vendas"]:
    vendedor = venda["vendedor"]
    valor = venda["valor"]

    if valor < 100:
        comissao = 0
    elif valor < 500:
        comissao = valor * 0.01
    else:
        comissao = valor * 0.05

    if vendedor in comissoes:
        comissoes[vendedor] += comissao
    else:
        comissoes[vendedor] = comissao

for vendedor, comissao in comissoes.items():
    print(f"{vendedor}: R$ {comissao:.2f}")