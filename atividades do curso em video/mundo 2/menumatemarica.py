saida = 0
valor_1 = int(input('Digite o primeiro valor: '))
valor_2 = int(input('Digite o segundo valor: '))
while saida != 5:
    print('''========================
[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR
[ 4 ] NOVOS NÚMEROS
[ 5 ] SAIR DO PROGRAMA
========================''')

    saida = int(input('Qual a sua opção: '))

    if saida == 1:
        resultado = valor_1 + valor_2
        print(f'{valor_1} + {valor_2} = {resultado}')
    elif saida == 2:
        resultado = valor_1 * valor_2
        print(f'{valor_1} x {valor_2} = {resultado}')
    elif saida == 3:
        maior = max(valor_1, valor_2)
        print(f'O maior valor é {maior}')
    elif saida == 4:
        print('Informe novos números:')
        valor_1 = float(input('Digite o primeiro valor: '))
        valor_2 = float(input('Digite o segundo valor: '))
    elif saida == 5:
        print('Saindo do programa...')
    else:
        print('Opção inválida!')