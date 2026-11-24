num = int(input('Digite um número: '))
divisor = []
soma = contador = 0
for c in range(1 , num + 1):
    if num % c == 0:
        divisor.append(c)
        contador += 1
        if c < 28:
            soma += c
print('Divisores:', *divisor)
print(f'Quantidade de divisores: {contador}')
print(f'Soma dos divisores menores que 28: {soma}')
