maior = 0
menor = 0
for c in range(1,6):
    numero = int(input(''))
    if c == 1:
        maior = numero
        menor = numero
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
print(maior)
print(menor)