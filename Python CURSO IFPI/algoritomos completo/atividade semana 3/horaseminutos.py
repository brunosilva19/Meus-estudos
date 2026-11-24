valor_min = float(input('Digite a quantidade de minutos: '))
horas = valor_min // 60
minuto = valor_min % 60

print(f'{valor_min} minutos corresponde a {horas:.0f} horas e {minuto:.0f} minutos.')