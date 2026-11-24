"""Calcular a compra de piso para um cômodo"""

from math import ceil
print(f'{'Calcular Piso':=^60}')
comprimento = float(input('Qual o comprimento: '))
largura = float(input('Qual a largura: '))
reserva = float(input('Percentual de reserva para perda: '))
cobertura_de_caixa = float(input('Cobertura de cada caixa: '))
preco_caixa = float(input('Preço da caixa: R$ '))
print("Calcular Piso" * 60)

area_comodo = comprimento * largura
area_de_perda = area_comodo + (area_comodo * reserva / 100)
quantidade_de_caixa = ceil(area_de_perda / cobertura_de_caixa)
valor_total = quantidade_de_caixa * preco_caixa
print("Calcular Piso" * 60)
print(f'A área do cômodo é: {area_comodo:.2f} m²')
print(f'A área com reserva é: {area_de_perda:.2f} m²')
print(f'A quantidade de caixas para {area_de_perda:.2f} m² é de: {quantidade_de_caixa}')
print(f'O valor para fazer {area_de_perda:.2f} m² é de: R$ {valor_total:.2f}')
