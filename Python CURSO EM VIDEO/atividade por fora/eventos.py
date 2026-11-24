"""Módulo para gerenciar eventos."""
from math import ceil
# entrada de dados
quantidade_de_pessoas = int(input('Quantidade de pessoas: '))
cap_veiculo = int(input('Capacidade de cada veículo: '))
alug = float(input('Aluguel por veículo: R$ '))
ocm = float(input('Orçamento: R$ '))

# calculos para o programa

quantidade_de_veiculo = ceil(quantidade_de_pessoas / cap_veiculo)
quantidade_de_vagas = quantidade_de_veiculo * cap_veiculo - quantidade_de_pessoas
custo_total = quantidade_de_veiculo * alug

if custo_total <= ocm:
    MENSAGEM_ORCAMENTO = '\033[32mOrçamento suficiente!\033[m'
    valor_restante = ocm - custo_total
    mensagem_valor = f'valor restante: R$ {valor_restante:.2f}'
else:
    MENSAGEM_ORCAMENTO = '\033[31mOrçamento insuficiente!\033[m'
    valor_faltante = custo_total - ocm
    mensagem_valor = f'Valor para poder fazer a viagem: R$ {valor_faltante:.2f}'

# saida pra o usuario

print(f'Veículos necessários: {quantidade_de_veiculo}')
print(f'Vagas vazias: {quantidade_de_vagas}')
print(f'Custo total: R$ {custo_total:.2f}')
print(MENSAGEM_ORCAMENTO)
print(mensagem_valor)
