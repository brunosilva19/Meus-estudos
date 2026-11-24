def calcular_imc(peso, altura):
    return peso / (altura ** 2)


def main():
    peso = float(input(''))
    altura = float(input(''))
    imc = calcular_imc(peso, altura)

    if imc < 18.5:
        print(imc)
        print('Abaixo do peso')
    elif imc < 25:
        print(imc)
        print('Peso normal')
    elif imc < 30:
        print(imc)
        print('Sobrepeso')
    elif imc < 35:
        print(imc)
        print('Obeso leve')
    elif imc < 40:
        print(imc)
        print('Obeso moderado')
    else:
        print(imc)
        print('Obeso mórbido')
if __name__ == '__main__':
    main()