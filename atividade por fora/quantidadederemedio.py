"""Calcular a quantidade de frascos de remédio"""
from math import ceil

quantidade_de_dias = int(input('Duração do tratamento: '))
doses_por_dia = int(input('Doses por dia: '))
quant_por_dose = float(input('Quantidade por doses em ml: '))
cap_do_frasco = float(input('Capacidade do frasco em ml: '))

total_de_doses = quantidade_de_dias * doses_por_dia
volume_necessario = total_de_doses * quant_por_dose
frascos_necessario = ceil(volume_necessario / cap_do_frasco)
quantidade_restante = cap_do_frasco * frascos_necessario - volume_necessario


print(f'O total de doses é: {total_de_doses}')
print(f'O volume necessário é: {volume_necessario:.2f} mL')
print(f'A quantidade de frascos é: {frascos_necessario}')
print(f'A quantidade restante é: {quantidade_restante:.2f} mL')
