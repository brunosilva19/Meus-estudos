def contar_caracteres(nome):
    return len(nome)


def main():
    nome = input("Digite o nome: ")
    estado_civil = input("Digite 1 para casado ou 2 para solteiro: ")

    total = contar_caracteres(nome)

    if estado_civil == "1":
        conjuge = input("Digite o nome do cônjuge: ")
        total = total + contar_caracteres(conjuge)

    print("Total de caracteres:", total)


if __name__ == "__main__":
    main()