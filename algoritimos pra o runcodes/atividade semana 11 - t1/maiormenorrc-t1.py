contador = menor_valor = maior_valor = 0
while True:
    num = int(input(''))
    if num == 0:
        break
    elif contador == 0:
        menor_valor = num
        maior_valor = num
    if num > maior_valor:
        maior_valor = num
    if num < menor_valor:
        menor_valor = num
    contador += 1
print(f'{maior_valor}')
print(f'{menor_valor}')
    