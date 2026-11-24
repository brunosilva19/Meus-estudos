valor = int(input('Qual o valor de saque: R$ '))
nota_50 = valor // 50
nota_20 = valor % 50 // 20
nota_10 = valor % 50 % 20 // 10
nota_5 = valor % 50 % 20 % 10 // 5
nota_1 = valor % 50 % 20 % 10 % 5 // 1
print(f'{"caixa eletrônico":=^40}')
print(f'Cédulas de R$ 50: {int(nota_50)}')
print(f'Cédulas de R$ 20: {int(nota_20)}')
print(f'Cédulas de R$ 10: {int(nota_10)}')
print(f'Cédulas de R$ 5: {int(nota_5)}')
print(f'Cédulas de R$ 1: {int(nota_1)}')
print(f'{'':=^40}')
print(f'Total entregue: R$ {valor:.2f}')
print(f'{'':=^40}')
