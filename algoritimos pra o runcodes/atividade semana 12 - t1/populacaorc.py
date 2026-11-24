def entrada_de_dados():
    pais_B = int(input(''))
    pais_A = int(input(''))

    return pais_B, pais_A


def calcular_dados(pais_B, pais_A):
    anos = 0
    while pais_B <= pais_A:
        pais_B += pais_B * 0.03
        pais_A += pais_A * 0.02
        anos += 1
        
    return anos


def main():
    pais_B, pais_A = entrada_de_dados()
    anos = calcular_dados(pais_B, pais_A)
    print(anos)


if __name__ == '__main__':
    main()