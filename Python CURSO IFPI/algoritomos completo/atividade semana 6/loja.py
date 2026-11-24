def calculos_da_loja(valor):
    # Pagamento à vista com 9% de desconto
    a_vista = valor * 0.91
    # Pagamento em 5 vezes sem juros
    parcela_5 = valor / 5
    # Pagamento em 10 vezes com 17% de juros
    valor_com_juros = valor * 1.17
    parcela_10 = valor_com_juros / 10
    return a_vista, parcela_5, parcela_10
def main():
    valor = float(input("Digite o valor da compra: R$ "))

    a_vista, parcela_5, parcela_10 = calculos_da_loja(valor)

    print(f"Valor à vista: R$ {a_vista:.2f}")
    print(f"Valor da prestação em 5 vezes: R$ {parcela_5:.2f}")
    print(f"Valor da prestação em 10 vezes: R$ {parcela_10:.2f}")


if __name__ == "__main__":
    main()