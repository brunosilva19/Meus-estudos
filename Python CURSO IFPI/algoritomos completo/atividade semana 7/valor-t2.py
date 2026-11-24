def separar_digitos(numero):
    centena = numero // 100
    dezena = (numero // 10) % 10
    unidade = numero % 10
    return centena, dezena, unidade


def main():
    numero = int(input("Digite um número: "))

    centena, dezena, unidade = separar_digitos(numero)

    quantidade = 0

    if numero >= 100:
        if centena % 2 == 0:
            quantidade = quantidade + 1

    if numero >= 10:
        if dezena % 2 == 0:
            quantidade = quantidade + 1

    if unidade % 2 == 0:
        quantidade = quantidade + 1

    print("Quantidade de dígitos pares:", quantidade)


if __name__ == "__main__":
    main()