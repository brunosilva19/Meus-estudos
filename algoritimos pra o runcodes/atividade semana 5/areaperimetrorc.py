def area_quadrado(a):
    """area quadrado"""
    area = a ** 2
    return area


def perimetro_quadrado(a):
    """"perimetro de um quadrado"""
    perimetro = 4 * a
    return perimetro


def main():
    """"dando valor para a variavel """
    lado = float(input(''))
    area = area_quadrado(lado)
    perimetro = perimetro_quadrado(lado)
    print(f'{area:>10.4f}')
    print(f'{perimetro:>10.4f}')


if __name__ == '__main__':
    main()
