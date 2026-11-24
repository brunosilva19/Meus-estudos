"""Calcular o tamanho de uma escada"""
from math import hypot

altura_da_parede = float(input('Qual a altura da parede: '))
base_parede = float(input('Distância da parede: '))

print(f'O comprimento necessário da escada é de: {hypot(altura_da_parede, base_parede):.2f} m.')
