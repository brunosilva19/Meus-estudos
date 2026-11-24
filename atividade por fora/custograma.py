# analisar valor para fazer um jardim circular
from math import pi

# entrada de dados do usuário
diametro = float(input('Diâmetro: '))
preco_da_grama = float(input('Preço da grama por m²: '))
orcamento = float(input('Orçamento: R$ '))

# calculos do programa
raio = diametro / 2
area = pi * raio ** 2
custo_da_grama = preco_da_grama * area

# saida 1 para o usuário
print(f'Raio: {raio:.2f} m')
print(f'Área do jardim: {area:.2f} m²')
print(f'Custo da grama: R$ {custo_da_grama:.2f}')

# condição para valor restante
if custo_da_grama > orcamento:
    resto_faltante = custo_da_grama - orcamento # valor que falta para concluir a obra
    print('Orçamento insuficiente!')
    print(f'Valor que falta pra concluir a obra: R$ {resto_faltante:.2f}')
else:
    valor_restante = orcamento - custo_da_grama  # valor que sobrou da obra
    print('Orçamento suficiente!')
    print(f'Valor que sobrou da obra: R$ {valor_restante:.2f}')
