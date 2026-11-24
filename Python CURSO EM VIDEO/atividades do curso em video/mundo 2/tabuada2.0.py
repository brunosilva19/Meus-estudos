"""Programa para fazer uma tabuada usando o larço for"""
#entrada de dados
numero = int(input('Digite o número que você quer saber a tabuada: '))
for c in range(1, 11):
    print(f'{numero} x {c:2d} = {numero*c}')
