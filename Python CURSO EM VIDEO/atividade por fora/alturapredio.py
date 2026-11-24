from math import tan , radians
distancia = float(input('Distância até o prédio: '))
angulo = float(input('Ângulo de visão: '))
altura_dos_olhos = float(input('Altura dos olhos: '))
altura_do_predio = tan(radians(angulo)) * \
    distancia + altura_dos_olhos
print(f'A altura aproximada do prédio: {altura_do_predio:.2f} m')
if altura_do_predio > 20:
    print('O prédio possui mais de 20 metros!')
else:
    print('O prédio não possui mais de 20 metros!')
