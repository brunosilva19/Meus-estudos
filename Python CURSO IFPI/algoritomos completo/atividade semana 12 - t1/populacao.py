def entrada_de_dados():
    pais_B = int(input('Digite a população de B: '))
    pais_A = int(input('Digite a população de A: '))

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
    print(f'Para o país B alcançar a população do país A vai precisar de {anos} anos')


if __name__ == '__main__':
    main()