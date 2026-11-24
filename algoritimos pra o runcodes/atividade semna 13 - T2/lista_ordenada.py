
def criar_lista():
    return []


def receber_dados(lista):
    while True:
        n = int(input(''))

        if n == 0:
            break

        for c in range(n):
            numero = float(input(''))
            lista.append(numero)

        break


def esta_ordenada(lista):
    return lista == sorted(lista)


def main():
    lista = criar_lista()
    receber_dados(lista)
    print('LISTA ORDENADA' if esta_ordenada(lista) else 'LISTA NÃO ORDENADA')


if __name__ == '__main__':
    main()
