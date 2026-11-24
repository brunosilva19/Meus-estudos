investimento_inicial = float(input('Investimento inicial: R$ '))
taxa_anual = float(input('Taxa anual (%): '))
quantidade_de_anos = int(input('Quantidade de anos: '))
meta = float(input('Meta financeira: R$ '))


saldo_atual = investimento_inicial

for investimento in range(quantidade_de_anos):
    saldo_atual = saldo_atual + (saldo_atual * (taxa_anual/100))
    print(f'Saldo no ano {investimento + 1}: R$ {saldo_atual:.2f}')
print(f'{'RELATÓRIO':=^40}')
print(f'Saldo final: R$ {saldo_atual:.2f}')
print(f'Rendimento total: R$ {saldo_atual - investimento_inicial:.2f}')
if saldo_atual >= meta:
    print('\033[32mMETA ATINGIDA!\033[m')
    print(f'Valor acima da meta: R$ {saldo_atual - meta:.2f}')
else:
    print('\033[31mMETA NÃO ATINGIDA!\033[m')
    print(f'Valor que falta para atingir a meta: R$ {meta - saldo_atual:.2f}')