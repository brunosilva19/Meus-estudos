from math import ceil
comprimento = float(input('Comprimento: '))
altura = float(input('Altura: '))
cober_lata = float(input('Cobertura da lata: '))
preco_lata = float(input('Preço da lata: R$ '))
orc = float(input('Orçamento: R$ '))
area = comprimento * altura  # Área da parede
quant_lata = ceil(area / cober_lata)  # quantidade de latas
custo_total = quant_lata * preco_lata  # valor total da obra
print(f'Área da parede: {area:.2f} m²')
print(f'Latas necessárias: {quant_lata}')
print(f'Custo total: R$ {custo_total:.2f}')
if custo_total <= orc:
    print('Orçamento suficiente!')
    valor_restante = orc - custo_total
    VALOR_TIPO = "restante"
else:
    print('Orçamento insuficiente!')
    valor_restante = custo_total - orc
    VALOR_TIPO = "faltante"
print(f'Valor {VALOR_TIPO}: R$ {valor_restante:.2f}')
