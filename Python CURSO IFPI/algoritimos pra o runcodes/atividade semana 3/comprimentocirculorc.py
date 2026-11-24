"""Calcula o comprimento da circunferência, a área do círculo e o volume da esfera."""
raio = float(input(""))
pi = 3.141592
comprimento = 2 * pi * raio
area = pi * raio ** 2
area_esfera = 4 * pi * raio ** 2
volume = (4 / 3) * pi * raio ** 3
print(f"{comprimento:.6f}")
print(f"{area:.6f}")
print(f"{area_esfera:.6f}")
print(f"{volume:.6f}")
