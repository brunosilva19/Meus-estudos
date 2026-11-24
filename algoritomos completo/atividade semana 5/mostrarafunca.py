def calcular(a, b, c):
    """somar valores"""
    return 2 * a + 5 * b - c
def main():
    """Pedir valores"""
    n1 = int(input('Digite o primeiro número: '))
    n2 = int(input('Digite o primeiro número: '))
    n3 = int(input('Digite o primeiro número: '))
    calculo = calcular(n1, n2, n3)
    print(calculo)
if __name__ == '__main__':
    main()
