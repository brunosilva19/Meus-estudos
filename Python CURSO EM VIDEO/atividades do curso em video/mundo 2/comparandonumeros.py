'''Comparando números'''

print(f"{'COMPARAR NÚMEROS':=^80}")

numero_1 = int(input('Digite o primeiro valor: '))
numero_2 = int(input('Digite o segundo valor: '))

if numero_1 > numero_2:
    print(f'O primeiro valor ({numero_1}) é maior que o segundo ({numero_2}).')
elif numero_2 > numero_1:
    print(f'O segundo valor ({numero_2}) é maior que o primeiro ({numero_1}).')
else:
    print(f'Não existe valor maior, os dois são iguais: {numero_1}.')
