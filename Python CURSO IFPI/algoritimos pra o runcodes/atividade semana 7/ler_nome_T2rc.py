def contar_caracteres(nome):
    return len(nome)


def main():
    nome = input("").strip()
    estado_civil = input("").strip()

    total = contar_caracteres(nome)

    if estado_civil == "1":
        conjuge = input("").strip()
        total2 = total + contar_caracteres(conjuge)
        print(total2)
    else:
        print(total)

if __name__ == "__main__":
    main()