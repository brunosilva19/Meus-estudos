def menu():
    return '''
========================================
         LANCHONETE - CARDÁPIO
========================================
CÓDIGO   PRODUTO             PREÇO (R$)
----------------------------------------
H        Hamburger           5.50
C        Cheeseburger        6.80
M        Misto Quente        4.50
A        Americano           7.00
Q        Queijo Prato        4.00
----------------------------------------
X        PARA TOTAL DA CONTA
========================================
'''
def opcoes_menu():
    valor = 0
    comida = []
    while True:
        ops = input('Digite o código do produto: ').strip().upper()[0]
        if ops == 'X':
            break
        elif ops == 'H':
            valor += 5.50
            comida.append('Hamburger --------- R$ 5.50')
        elif ops == 'C':
            valor += 6.80
            comida.append('Cheeseburger --------- R$ 6.80')
        elif ops == 'M':
            valor += 4.50
            comida.append('Misto Quente --------- R$ 4.50')
        elif ops == 'A':
            valor += 7.00
            comida.append('Americano --------- R$ 7.00')
        elif ops == 'Q':
            valor += 4.00
            comida.append('Queijo Prato --------- R$ 4.00')
        else:
            print('Categoria Inválida')    
    return valor,comida
def main():
    print(menu())
    valor,comida = opcoes_menu()
    print('\n' + f'{"NOTA":=^40}')
    for c in comida:
        print(f'{c}')
    print('=' * 40)
    print(f'TOTAL DA CONTA: R$ {valor:.2f}')
    print('=' * 40)
if __name__ == '__main__':
    main()