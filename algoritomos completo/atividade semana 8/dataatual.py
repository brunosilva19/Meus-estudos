from datetime import date

print('============== Comparando datas ===============')
print('Digite a primeira data')
dia1 = int(input('Dia: '))
mes1 = int(input('Mês: '))
ano1 = int(input('Ano: '))

print('============ Digite a segunda data ============')
dia2 = int(input('Dia: '))
mes2 = int(input('Mês: '))
ano2 = int(input('Ano: '))

primeira_data = date(dia1, mes1, ano1)
segunda_data = date(dia2, mes2, ano2)

if primeira_data > segunda_data:
    print(f'{dia1}/{mes1}/{ano1}')
elif segunda_data > primeira_data:
    print(f'{dia2}/{mes2}/{ano2}')
else:
    print('As duas datas são iguais.')