def maximo_valor(valor1, valor2, valor3, valor4, valor5):
    return max(valor1,valor2,valor3,valor4,valor5)

def minino_valor(valor1, valor2, valor3, valor4, valor5):
    return min(valor1, valor2, valor3, valor4, valor5)

def media_aritmetica(valor1, valor2, valor3, valor4, valor5):
    media = (valor1 + valor2 + valor3 + valor4 + valor5) / 5
    return media

def main():
    valor1 = int(input(""))
    valor2 = int(input(""))
    valor3 = int(input(""))
    valor4 = int(input(""))
    valor5 = int(input(""))
    max = maximo_valor(valor1, valor2, valor3, valor4, valor5)
    min = minino_valor(valor1, valor2, valor3, valor4, valor5)
    media = media_aritmetica(valor1, valor2, valor3, valor4, valor5)
    print(f'{max}\n{min}\n{media}')
if __name__ == '__main__':
    main()
