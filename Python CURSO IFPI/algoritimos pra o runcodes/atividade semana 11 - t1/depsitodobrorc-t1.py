def ler_dados_iniciais():
    deposito_inicial = float(input(''))
    taxa = float(input(''))
    return deposito_inicial, taxa


def mostrar_relatorio(deposito_inicial, taxa):
    saldo_inicial = deposito_inicial
    anos = 0
    while deposito_inicial <= 2 * saldo_inicial:
        deposito_inicial += deposito_inicial * taxa / 100
        anos += 1
    return anos

def main():
    deposito_inicial, taxa = ler_dados_iniciais()
    print(mostrar_relatorio(deposito_inicial, taxa))


if __name__ == '__main__':
    main()
