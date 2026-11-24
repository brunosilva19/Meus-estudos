raio = float(input("Digite o raio do círculo: "))
pi = 3.141592
comprimento = 2 * pi * raio
area = pi * raio ** 2
area_esfera = 4 * pi * raio ** 2
volume = (4 / 3) * pi * raio ** 3
print(f"O comprimento do círculo é: {comprimento:.6f}")
print(f"A área do círculo é: {area:.6f}")
print(f"A área da esfera é: {area_esfera:.6f}")
print(f'O volume da esfera é: {volume:.6f}')
