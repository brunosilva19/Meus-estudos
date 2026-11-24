def calcular_total(preco_maca, preco_banana):
    return (3 * preco_maca) + (2 * preco_banana)


def main():
    preco_maca = float(input(""))
    preco_banana = float(input(""))

    total = calcular_total(preco_maca, preco_banana)

    print(f"{total:.2f}")


main()