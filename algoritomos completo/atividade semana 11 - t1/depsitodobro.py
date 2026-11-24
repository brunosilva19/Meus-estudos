def ler_dados_iniciais():
    deposito_inicial = float(input('Qual o depósito inicial: R$ '))
    taxa = float(input('Qual a taxa de juros ao ano: '))
    return deposito_inicial, taxa


def mostrar_relatorio(deposito_inicial, taxa):
    saldo_inicial = deposito_inicial
    anos = 0
    print(f'Inicio: R$ {deposito_inicial:.2f}')

    while deposito_inicial <= 2 * saldo_inicial:
        deposito_inicial += deposito_inicial * taxa / 100
        anos += 1
        print(f'{anos} Ano: R$ {deposito_inicial:.2f}')


def main():
    deposito_inicial, taxa = ler_dados_iniciais()
    mostrar_relatorio(deposito_inicial, taxa)


if __name__ == '__main__':
    main()
