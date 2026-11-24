"""Calcular o preço de uma pizza por centimentro quadrado"""
from math import pi
diametro_da_pizza = float(input('Diâmetro da pizza: '))
preco = float(input('Preço da pizza: R$ '))

raio = diametro_da_pizza / 2
area = pi * raio ** 2
preco_por_centimetro = preco / area

print(f'Raio: {raio:.2f} cm')
print(f'Area da pizza: {area:.2f} cm²')
print(f'Preço por cm²: R$ {preco_por_centimetro:.3f}')
