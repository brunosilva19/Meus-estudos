lista_original = []
lista_multiplo = []

def multiplica_constante(lista_original, constante):
    return [numero * constante for numero in lista_original]


lista_original = []

while True:
    num = int(input('Digite um número: '))
    if num == 0:
        break
    lista_original.append(num)

valor = int(input('Digite o valor que vai usar para multiplicar na lista: '))
lista_multiplo = multiplica_constante(lista_original, valor)
print(lista_multiplo)