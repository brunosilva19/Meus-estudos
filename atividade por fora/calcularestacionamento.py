# PARA CALCULAR A COBRAÇA DO ESTACIONAMENTO
from math import ceil
tempo_estacionamento = int(input('Duração do estacionamento(min): '))
# calculos para o programa
horas = tempo_estacionamento // 60
minutos = tempo_estacionamento % 60
# saidada para o usuário
print(f'Tempo de estacionamento: {horas:02d}h {minutos:02d}min')
if tempo_estacionamento <= 120:
    tempo_adicional = 0
    horas_adicional_cobrada = 0
    valor_de_estacionamento = 8.00
else:
    tempo_adicional = tempo_estacionamento - 120
    horas_adicionais_cobrada = ceil(tempo_adicional / 60)
    valor_de_estacionamento = 8.00 + 3.00 * horas_adicionais_cobrada
print(f'Tempo adicional: {tempo_adicional} minutos')
print(f'Horas adicionais cobradas: {horas_adicionais_cobrada}')
print(f'Valor do estacionamento: R$ {valor_de_estacionamento:.2f}')
