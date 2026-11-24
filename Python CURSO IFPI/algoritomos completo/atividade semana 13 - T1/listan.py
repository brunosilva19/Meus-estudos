n = int(input('valor: '))

lista = [0] * n
print(lista)

lista = list(range(1, n + 1))
print(lista)

lista = []
for i in range(n):
    valor = int(input(f'valor {i + 1}: '))
    lista.append(valor)
print(lista)

lista = []
for i in range(n):
    valor = int(input(f'valor {i + 1}: '))
    lista.insert(0, valor)
print(lista)