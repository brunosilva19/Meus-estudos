#entrada de dados

horas = int(input('Horas: '))
minutos = int(input('Minutos: '))
segundos = int(input('Segundos: '))

#calculos para o programa

total_segundos = horas * 3600 + minutos * 60 + segundos

# saida para o usuario

print(f'Se passaram {total_segundos} segundos desde a ultima meia noite.')