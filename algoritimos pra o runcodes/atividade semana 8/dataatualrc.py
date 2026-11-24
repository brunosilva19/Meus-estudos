from datetime import date

dia1 = int(input(''))
mes1 = int(input(''))
ano1 = int(input(''))


dia2 = int(input(''))
mes2 = int(input(''))
ano2 = int(input(''))

primeira_data = date(ano1, mes1, dia1)
segunda_data = date(ano2, mes2, dia2)

if primeira_data > segunda_data:
    print(f'{dia1}/{mes1}/{ano1}')
elif segunda_data > primeira_data:
    print(f'{dia2}/{mes2}/{ano2}')
else:
    print(f'{dia1}/{mes1}/{ano1}')