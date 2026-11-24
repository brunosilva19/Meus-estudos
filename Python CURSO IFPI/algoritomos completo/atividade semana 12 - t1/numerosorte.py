def dados():
    return int(input('Digite a data de deu nascimento[dd/mm/aaaa]: '))


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
    print(f'O númeor da sorte para essa data de nascimento é: {calculos(idade)}')


if __name__ == "__main__":
    main()