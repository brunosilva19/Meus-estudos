from math import pi
raio = float(input('Qual a medida do raio: '))
alt = float(input('Qual a altura do cilindro: '))

area_da_base = pi * pow(raio, 2)
volume = area_da_base * alt

print(f'A Área da base é de {area_da_base:.2f}')
print(f'O volume do cilindro é de {volume:.2f}')
