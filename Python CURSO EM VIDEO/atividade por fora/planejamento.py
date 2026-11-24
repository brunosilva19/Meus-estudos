"""Calcula os custos e os dados de uma excursão."""

from math import ceil
from random import randint
#entradas do usuário
codigo = input('Código da excursão: ')
quantidade_de_participantes = int(input('Quantidade de participantes: '))
capacidade_do_carro = int(input('Capacidade por veículo: '))
distancia = float(input('Distância de ida: '))
consumo_do_carro = float(input('Consumo do veículo: '))
preco_combustivel = float(input('Preço do combustível: R$ '))
pedagio = float(input('Pedágios de ida e volta por veículo: R$ '))
reserva_gastos = float(input('Reserva para gastos inesperados: '))
horas_saida = int(input('Hora da saída: '))
minutos_saida = int(input('Minuto da saída: '))
duraca_da_viagem = int(input('Duração da viagem de ida: '))
#variaveis e calculos
carros_necessarios = ceil(quantidade_de_participantes / capacidade_do_carro)
vagas_vazias = capacidade_do_carro * \
    carros_necessarios - quantidade_de_participantes
combustivel = (distancia * 2) / consumo_do_carro * carros_necessarios
custo_combustivel = combustivel * preco_combustivel
custo_pedagio = pedagio * carros_necessarios
sub_total = custo_pedagio + custo_combustivel
valor_reserva = sub_total * reserva_gastos / 100
custo_final = sub_total + valor_reserva
valor_por_pessoa = custo_final / quantidade_de_participantes
total_minutos = horas_saida * 60 + minutos_saida + duraca_da_viagem
hora_termino = (total_minutos // 60) % 24
minuto_termino = total_minutos % 60
sorteio = randint(1000, 9999)


print(f'Tipo primitivo do código: {type(codigo)}')
print(f'Possui somente letras e números? {codigo.isalnum()} ')
print(f'Está completamente em maiúsculas? {codigo.isupper()}')
print(f'Veículos necessários: {carros_necessarios}')
print(f'Vagas vazias: {vagas_vazias}')
print(f'Combustível necessário: {combustivel:.2f}')
print(f'Custo do combustível: {custo_combustivel:.2f}')
print(f'Custo dos pedágios: {custo_pedagio:.2f}')
print(f'Subtotal da excursão: {sub_total:.2f}')
print(f'Valor da reserva:{valor_reserva:.2f}')
print(f'Custo final: {custo_final:.2f}')
print(f'Valor por participante: {valor_por_pessoa:.2f}')
print(f'Horário de chegada: {hora_termino:02d}:{minuto_termino:02d}')
print(f'Código de confirmação: {sorteio}')
