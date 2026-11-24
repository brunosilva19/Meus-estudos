def entra_de_dados():
    num = int(input(''))
    return num

def somando():
    soma = 0
    while True:
        num = entra_de_dados()
        if num == 0:
            break
        soma += num
    return soma

def main():
    valor = somando()
    print(valor)

if __name__ == '__main__':
    main()