#entrada de dados

valor1 = float(input('Digite um valor: '))
valor2 = float(input('Digite outro valor: '))

#calculo para o programa

divisao_inteira = valor1 // valor2
resto_divisao = valor1 % valor2

#saida para o usuario

print(f'A parte intera de {valor1} por {valor2} é {divisao_inteira:.4f}')
print(f'O reto da divisão de {valor1} por {valor2} é {resto_divisao:.4f}')