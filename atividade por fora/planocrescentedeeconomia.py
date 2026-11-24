deposito = float(input('Primeiro depósito: R$ '))
valor_mes = float(input('Aumento mensal: R$ '))
meses = int(input('Quantidade de meses: '))
meta = float(input('Meta: R$ '))

saldo_final = 0
print(f'{'VALORES':=^40}')
for c in range(meses):
    print(f'Mês {c + 1}: R$ {deposito:.2f}')
    saldo_final += deposito
    if c < meses - 1:
        deposito += valor_mes     
print('=' * 40)
print(f'Total economizado: R$ {saldo_final:.2f}')
print(f'Último depósito: R$ {deposito:.2f}')
if saldo_final >= meta:
    print('\033[32mMETA ATINGIDA!\33[m')
    print(f'Valor acima da meta: R$ {saldo_final - meta:.2f}')
else:
    print('\033[31mMETA NÃO ATINGIDA!\33[m')
    print(f'Valor que falta para atingir a meta: R$ {meta - saldo_final:.2f}')