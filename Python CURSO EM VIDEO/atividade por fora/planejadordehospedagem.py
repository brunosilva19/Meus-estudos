from random import randint
# entrada de dados
responsavel = input('Responsável: ').strip()
destino = input('Destino: ').strip()
diaria = float(input('Preço da diária: R$ '))
quantidade_de_dias = int(input('Quantidade de dias: '))
viajantes = int(input('Quantidade de viajantes: '))
orcamento = float(input('Orçamento: R$ '))
horas = int((input('Hora da saída: ')))
minutos = int(input('Minuto da saída: '))
tempo_de_viagem = int(input('Duração da viagem(min): '))
# randomizar um codigo
codigo = randint(1000, 9999)

# calculos para o programa

subtotal = diaria * quantidade_de_dias
total_minutos = horas * 60 + minutos + tempo_de_viagem
horas_chegada = (total_minutos // 60) % 24
minutos_chegada = total_minutos % 60
# condição de desconto

if quantidade_de_dias >= 5:
    desconto = subtotal * 0.1
else:
    desconto = 0

# calculos para o programa

custo_final = subtotal - desconto
valor_por_viajante = custo_final / viajantes

# saida pra o usuario

print(f'Responsável: {responsavel.title()}')
print(f'Destino: {destino.title()}')
print(f'Subtotal da hospedagem: R$ {subtotal:.2f}')
print(f'Desconto: R$ {desconto:.2f}')
print(f'Custo final: R$ {custo_final:.2f}')
print(f'Valor por viajante: R$ {valor_por_viajante:.2f}')
print(f'Horário de chegada: {horas_chegada:02d}:{minutos_chegada:02d}')

# condição do orçamento

if custo_final > orcamento:
    print('\033[31mA hospedagem não cabe no orçamento!\033[m')
    print(f'Valor que falta para poder fazer a viagem: R$ {custo_final - orcamento:.2f}')
else:
    print('\033[32mA hospedagem cabe no orçamento!\033[m')
    print(f'Valor restante: R$ {orcamento - custo_final:.2f}')

print(f'Código de confirmação: {codigo}')
