from datetime import datetime, date

valor = float(input("Digite o valor: "))
data_vencimento = input("Digite a data de vencimento (dd/mm/aaaa): ")

vencimento = datetime.strptime(data_vencimento, "%d/%m/%Y").date()
hoje = date.today()

dias_atraso = (hoje - vencimento).days

if dias_atraso > 0:
    juros = valor * 0.025 * dias_atraso
else:
    juros = 0

valor_total = valor + juros

print(f"Dias de atraso: {max(dias_atraso, 0)}")
print(f"Juros: R$ {juros:.2f}")
print(f"Valor total: R$ {valor_total:.2f}")