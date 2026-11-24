numero = int(input(''))
invertido = 0

while numero > 0:
    ultimo = numero % 10
    invertido = invertido * 10 + ultimo
    numero = numero // 10
print(invertido)