"""Calculate the travel time in days and hours."""

distancia = float(input(''))
velocidade = float(input(''))

tempo_total = distancia / velocidade

dias = tempo_total // 24
horas = tempo_total % 24

print(f'{dias:.0f} dias e {horas:.0f} horas')
