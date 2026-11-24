from math import sqrt

a1 = float(input('Coordenada x do ponto A: '))
a2 = float(input('Coordenada y do ponto A: '))
b1 = float(input('Coordenada x do ponto B: '))
b2 = float(input('Coordenada y do ponto B: '))

distancia = sqrt(pow(a1 - b1, 2) + pow(a2 - b2, 2))

print(f'A distância entre os pontos é de: {distancia:.2f}')
