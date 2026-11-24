def calculos_da_loja(valor):
    a_vista = valor * 0.91
    parcela_5 = valor / 5
    valor_com_juros = valor * 1.17
    parcela_10 = valor_com_juros / 10
    return a_vista, parcela_5, parcela_10
def main():
    valor = float(input(""))

    a_vista, parcela_5, parcela_10 = calculos_da_loja(valor)

    print(f"{a_vista:.2f}")
    print(f"{parcela_5:.2f}")
    print(f"{parcela_10:.2f}")


if __name__ == "__main__":
    main()