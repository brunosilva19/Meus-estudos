valor = float(input('Qual é o seu salári R$: '))
if valor <= 1250:
    salario = valor + valor * 0.15
else:
    salario = valor + valor * 0.1
print(f'Quem ganhava R$ {valor:.2f} passa a ganhar R$ {salario:.2f} agora.')