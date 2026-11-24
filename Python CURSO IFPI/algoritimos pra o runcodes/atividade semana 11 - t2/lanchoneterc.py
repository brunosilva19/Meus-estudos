def menu():
    return print('''
CÓDIGO  PRODUTO         PREÇO (R$)
H       Hamburger       5,50
C       Cheeseburger    6,80
M       Misto Quente    4,50
A       Americano       7,00
Q       Queijo Prato    4,00
X       PARA TOTAL DA CONTA''')
def opcoes_menu():
    valor = 0
    while True:
        menu()
        ops = input().strip().upper()[0]
        if ops == 'X':
            break
        elif ops == 'H':
            valor += 5.50
        elif ops == 'C':
            valor += 6.80
        elif ops == 'M':
            valor += 4.50
        elif ops == 'A':
            valor += 7.00
        elif ops == 'Q':
            valor += 4.00
        else:
            print('Categoria Inválida')
    return valor


def main():
    print(f'{opcoes_menu():.2f}')

if __name__ == '__main__':
    main()