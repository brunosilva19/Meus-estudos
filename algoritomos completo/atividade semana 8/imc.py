def calcular_imc(peso, altura):
    return peso / (altura ** 2)


def main():
    peso = float(input('Digite seu peso [em kg]: '))
    altura = float(input('Digite sua altura [em m]: '))
    imc = calcular_imc(peso, altura)

    if imc < 18.5:
        print('Abaixo do peso')
    elif imc < 25:
        print('Peso normal')
    elif imc < 30:
        print('Sobrepeso')
    elif imc < 35:
        print('Obeso leve')
    elif imc < 40:
        print('Obeso moderado')
    else:
        print('Obeso mórbido')
if __name__ == '__main__':
    main()