contador = menor_valor = maior_valor = 0
print('''======Digite um número=====
[aperte 0 para encerrar]:''')
while True:
    num = int(input('Número: '))
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
print(f'O maior valor é: {maior_valor}')
print(f'O menor valor é: {menor_valor}')
    