def vogal(valor):
    return valor in "AEIOUaeiou"

def consoante(valor):
    return valor in "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"

def numero(valor):
    return valor in "0123456789"

def simbolo(valor):
    return not vogal(valor) and not consoante(valor) and not numero(valor)

def main():
    valor = input("Digite um caractere: ")

    if vogal(valor):
        print("vogal")

    elif consoante(valor):
        print("consoante")

    elif numero(valor):
        print("número")

    elif simbolo(valor):
        print("símbolo")

if __name__ == "__main__":
    main()