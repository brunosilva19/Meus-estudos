def calcular_idade(anoatual, anousuario):
    return anoatual - anousuario
def main():
    diaatual = int(input(''))
    mesatual = int(input(''))
    anoatual = int(input(''))
    diausuario = int(input(''))
    mesusuario = int(input(''))
    anousuario = int(input(''))
    if mesatual > mesusuario:
        print(calcular_idade(anoatual, anousuario))
    elif mesatual < mesusuario:
        print(calcular_idade(anoatual, anousuario) - 1)
    elif mesatual == mesusuario and diausuario < diaatual:
        print(calcular_idade(anoatual, anousuario))
    elif mesatual == mesusuario and diausuario > diaatual:
        print(calcular_idade(anoatual, anousuario) - 1)
    elif mesatual == mesusuario and diausuario == diaatual:
        print(calcular_idade(anoatual, anousuario))
if __name__ == '__main__':
    main()