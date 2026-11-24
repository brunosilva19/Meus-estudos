def entrada_de_dados():
    salario = float(input('Digite seu salario: R$ '))
    valor_divida = float(input('Digite o valor da divida: R$ '))
    return salario, valor_divida


def calcular_situacao(salario, valor_divida):
    ano, mes = 2016, 10
    while valor_divida < salario:
        valor_divida += valor_divida * 0.15
        if mes == 3:
            salario += salario * 0.05
        mes += 1
        if mes > 12:
            mes = 1
            ano += 1
    return salario, valor_divida, mes, ano


def exibir_resultado(salario, valor_divida, mes, ano):
    print('\n' + '=' * 34)
    print('         RESULTADO FINAL')
    print('=' * 34)
    print(f'Dívida:  R$ {valor_divida:,.2f}')
    print(f'Salário: R$ {salario:,.2f}')
    print(f'Data:    {mes:02d}/{ano}')
    print('=' * 34)


def main():
    salario, valor_divida = entrada_de_dados()
    salario, valor_divida, mes, ano = calcular_situacao(salario, valor_divida)
    exibir_resultado(salario, valor_divida, mes, ano)

if __name__ == '__main__':
    main()