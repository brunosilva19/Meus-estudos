def maximo_valor(valor1, valor2, valor3, valor4, valor5):
    return max(valor1,valor2,valor3,valor4,valor5)

def minino_valor(valor1, valor2, valor3, valor4, valor5):
    return min(valor1, valor2, valor3, valor4, valor5)

def media_aritmetica(valor1, valor2, valor3, valor4, valor5):
    media = (valor1 + valor2 + valor3 + valor4 + valor5) / 5
    return media

def main():
    valor1 = int(input("Digite o 1° número: "))
    valor2 = int(input("Digite o 2° número: "))
    valor3 = int(input("Digite o 3° número: "))
    valor4 = int(input("Digite o 4° número: "))
    valor5 = int(input("Digite o 5° número: "))
    max = maximo_valor(valor1, valor2, valor3, valor4, valor5)
    min = minino_valor(valor1, valor2, valor3, valor4, valor5)
    media = media_aritmetica(valor1, valor2, valor3, valor4, valor5)
    print(f'Dos números digitados o maior valor é {max} e o menor é {min} e a média aritimética é {media}')
if __name__ == '__main__':
    main()
