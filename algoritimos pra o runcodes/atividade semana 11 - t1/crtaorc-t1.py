def entrada_de_dados():
    salario = float(input(''))
    valor_divida = float(input(''))
    return salario, valor_divida


def calcular_situacao(salario, valor_divida):
    ano, mes = 2016, 10
    while valor_divida < salario:
        valor_divida += valor_divida * 0.15
        mes += 1
        if mes > 12:
            mes = 1
            ano += 1
        if mes == 3:
            salario += salario * 0.05
    return salario, valor_divida, mes, ano


def exibir_resultado(salario, valor_divida, mes, ano):
    print(f'{mes}/{ano}')


def main():
    salario, valor_divida = entrada_de_dados()
    salario, valor_divida, mes, ano = calcular_situacao(salario, valor_divida)
    exibir_resultado(salario, valor_divida, mes, ano)


if __name__ == '__main__':
    main()