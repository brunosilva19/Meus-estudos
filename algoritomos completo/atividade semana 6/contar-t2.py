def contar_caracteres(frase):
    frase = frase.strip()
    return len(frase)


def main():
    frase = input("Digite uma frase: ")
    quantidade = contar_caracteres(frase)

    print(f"Número de caracteres: {quantidade}")
if __name__ == '__main__':
    main()