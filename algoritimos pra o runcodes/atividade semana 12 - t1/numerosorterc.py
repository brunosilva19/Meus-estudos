def dados():
    return int(input(''))


def calculos(idade):
    soma = 0
    cont = 0
    while cont != 8:
        soma += idade % 10
        idade = idade // 10
        cont += 1
    return soma


def main():
    idade = dados()
    print(calculos(idade))


if __name__ == "__main__":
    main()