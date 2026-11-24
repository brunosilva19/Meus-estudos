def separar_digitos(numero):
    dezena = numero // 10
    unidade = numero % 10
    return dezena, unidade


def main():
    numero = int(input("Digite um número entre 10 e 99: "))

    dezena, unidade = separar_digitos(numero)

    if dezena % 2 == 0 and unidade % 2 == 0:
        print("Nenhum dígito é ímpar.")

    elif dezena % 2 != 0 and unidade % 2 != 0:
        print("Os dois dígitos são ímpares.")

    else:
        print("Apenas um dígito é ímpar.")


if __name__ == "__main__":
    main()