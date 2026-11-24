def verificar_retangulo(base, altura):
    return base != altura

def perimetro(base, altura):
    return 2 * (base + altura) 

def area(base, altura):
    return base * altura

def main():
    base = float(input('Qual a medida da base: '))
    altura = float(input('Qual a medida da altura: '))
    if verificar_retangulo(base, altura):
        if verificar_retangulo(base, altura).is_integer() :
            print(f'{int(perimetro(base, altura))} - {int(area(base, altura))}')
        else:
            print(f'{perimetro(base, altura)} - {area(base, altura)}')
    else:
        print('QUADRADO')
if __name__ == '__main__':
    main()


