def calcular_total(preco_maca, preco_banana):
    return (3 * preco_maca) + (2 * preco_banana)


def main():
    preco_maca = float(input("Digite o preço de uma maçã: R$ "))
    preco_banana = float(input("Digite o preço de uma banana: R$ "))

    total = calcular_total(preco_maca, preco_banana)

    print(f"Total da compra: R$ {total:.2f}")
if __name__=="main":
    main()