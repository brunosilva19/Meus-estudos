n = int(input(''))


lista = [0] * n
print(lista)

lista = list(range(1, n + 1))
print(lista)

lista = []
for i in range(n):
    valor = int(input(''))
    lista.append(valor)
print(lista)

lista = []
for i in range(n):
    valor = int(input(''))
    lista.insert(0, valor)
print(lista)