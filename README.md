# Desafio Técnico

Aqui estão os 3 desafios feitos em Python.

## Desafio 1 - Comissão de vendedores

Nesse desafio eu leio o arquivo `vendas.json` e percorro todas as vendas.

Para cada venda, calculo a comissão de acordo com as regras:

- abaixo de R$ 100,00: sem comissão
- abaixo de R$ 500,00: 1%
- a partir de R$ 500,00: 5%

Depois vou somando os valores por vendedor e mostro o total de comissão de cada um.

## Desafio 2 - Controle de estoque

Nesse desafio eu uso o arquivo `estoque.json` para buscar os produtos pelo código.

O programa permite escolher se a movimentação é uma entrada ou uma saída e informa a quantidade movimentada.

Também fiz algumas validações simples, como verificar se o produto existe e impedir uma saída maior que a quantidade disponível.

No final, o estoque atualizado é salvo no `estoque.json`.

Também deixei um `movimentacoes.json` para guardar o histórico das movimentações feitas.

## Desafio 3 - Cálculo de juros

Nesse desafio o programa recebe um valor e uma data de vencimento.

Ele compara a data informada com a data atual e calcula quantos dias estão em atraso.

Se estiver vencido, aplica 2,5% de juros por dia.

Se ainda não estiver vencido, os juros ficam em zero.

## Como executar

Cada desafio pode ser executado separado:

```bash
python Desafio1.py
python Desafio2.py
python Desafio3.py
```
