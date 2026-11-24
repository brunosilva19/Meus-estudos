primeiro_numero = int(input(''))
segundo_numero = int(input(''))

for c in range(primeiro_numero, segundo_numero + 1):
    cont = 1
    divisores = 0
    while cont <= c:
        if c % cont == 0:
            divisores += 1
        cont += 1
    if divisores == 2:
        print(c)