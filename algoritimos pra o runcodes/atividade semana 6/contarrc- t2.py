def contar_caracteres(frase):
    frase = frase.strip()
    return len(frase)


def main():
    frase = input("")
    quantidade = contar_caracteres(frase)

    print(f"{quantidade}")
if __name__ == '__main__':
    main()