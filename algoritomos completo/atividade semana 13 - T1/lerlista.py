def entrada_dado():
    return int(input('Digite um valor: '))

def lista():
    return []


def add_lista(valores, num):
    valores.append(num)


def soma(valores):
    total = 0
    for num in valores:
        total += num
    return total


def multiplicar(valores):
    total = 1
    for num in valores:
        total *= num
    return total


def main():
    valores = lista()
    for c in range(1,11):
        numero = entrada_dado()
        add_lista(valores, numero)

    print(valores)
    print(soma(valores))
    print(multiplicar(valores))


if __name__ == '__main__':
    main()