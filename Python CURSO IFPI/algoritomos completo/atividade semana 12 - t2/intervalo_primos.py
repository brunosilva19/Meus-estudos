def dados():
    primeiro_numero = int(input('Digite o primeiro numero: '))
    segundo_numero = int(input('Digite o segundo numero: '))
    return primeiro_numero, segundo_numero

def calculos(primeiro_numero, segundo_numero):
    for c in range(primeiro_numero, segundo_numero + 1):
        cont = 1
        divisores = 0
        while cont <= c:
            if c % cont == 0:
                divisores += 1
            cont += 1
        if divisores == 2:
            print(c)

def main():
    primeiro_numero, segundo_numero = dados()
    valor = calculos(primeiro_numero, segundo_numero)
    
if __name__ == '__main__':
    main()