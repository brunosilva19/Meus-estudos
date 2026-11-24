
def criar_lista():
    return []


def receber_dados(lista):
    while True:
        n = int(input('Digite a quantidade de elementos da lista: '))

        if n == 0:
            break

        for _ in range(n):
            valor = input('Digite os elementos da lista: ')
            try:
                valor = float(valor)
            except ValueError:
                pass
            lista.append(valor)
        break

def esta_ordenada(lista):
    return lista == sorted(lista)


def main():
    lista = criar_lista()
    receber_dados(lista)
    print('LISTA ORDENADA' if esta_ordenada(lista) else 'LISTA NÃO ORDENADA')


if __name__ == '__main__':
    main()
