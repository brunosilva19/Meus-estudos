"""Calcula o tempo estimado de uma viagem."""

distancia = float(input('Qual a distância em: KM '))
velocidade = float(input('Qual a sua velocidade em: km/h '))

tempo_total = distancia / velocidade

dias = tempo_total // 24
horas = tempo_total % 24

print(f'A viagem vai levar: {dias:.0f} dias e {horas:.0f} h.')
