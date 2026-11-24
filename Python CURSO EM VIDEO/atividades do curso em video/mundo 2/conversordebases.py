""""programa para converte bases"""
#entrada de dados
numero = int(input('Digite um número: '))
ops = int(input('''Escolha uma das bases para a converção:
[ 1 ] converter para BINÁRIO
[ 2 ] converter para OCTAL
[ 3 ] converter para HEXADECIMAL
Sua opção: '''))
if ops == 1:
    print(f'{numero} convertido em BINÁRIO é {bin(numero)[2:]}')
elif ops == 2:
    print(f'{numero} convertido em OCTAL é {oct(numero)[2:]}')
elif ops == 3:
    print(f'{numero} convertido em HEXADECIMAL é {hex(numero)[2:]}')
else:
    print('\033[31mOpção invalida. tente novamente!\033[m')
