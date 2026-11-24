def calcular_idade(anoatual, anousuario):
    return anoatual - anousuario
def main():
    diaatual = int(input('Qual o dia de hoje: '))
    mesatual = int(input('Qual o mês atual: '))
    anoatual = int(input('Qual o ano atual: '))
    print('==================Usuário==================')
    diausuario = int(input('Qual o dia do seu aniversário: '))
    mesusuario = int(input('Qual o mês do seu aniversário: '))
    anousuario = int(input('Qual o ano do seu aniversário: '))
    if mesatual > mesusuario:
        print('caiu no if')
        print(calcular_idade(anoatual, anousuario))
    elif mesatual < mesusuario:
        print('caiu no elife 1')
        print(calcular_idade(anoatual, anousuario) - 1)
    elif mesatual == mesusuario and diausuario < diaatual:
        print('caiu no elife 2')
        print(calcular_idade(anoatual, anousuario))
    elif mesatual == mesusuario and diausuario > diaatual:
        print('caiu no elife 3')
        print(calcular_idade(anoatual, anousuario) - 1)
    elif mesatual == mesusuario and diausuario == diaatual:
        print('caiu no elife 4')
        print(calcular_idade(anoatual, anousuario))
if __name__ == '__main__':
    main()