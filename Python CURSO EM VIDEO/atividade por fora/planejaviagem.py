# Planejador de viagem em grupo
from random import randint
# entradas de informação do usuário
destino = input('Qual o destino: ')
distancia = float(input('Qual a distancia da viagem(Km): '))
consumo_v = float(input('Qual o consumo do veículo(Km/l): '))
preco_combustivel = float(input('Qual o preço do combustível: R$ '))
pessoas = int(input('Quantidade de viajantes: '))
orc = float(input('Orçamento: R$ '))
# codigo da viagem
codigo = randint(1000, 9999)
# calculos para o programa funcionar corretamente
distancia_total = distancia * 2  # a distância de ida e volta
combustivel_necessario = distancia_total / consumo_v
custo_total = combustivel_necessario * preco_combustivel
valor_por_viajante = custo_total / pessoas
# saida e informação para o usuário
print("==============================INFORMAÇÕES==============================")
print(f'O destino da viagem é: {destino.capitalize()}')
print(f'A distância de ida e volta é de: {distancia_total:.2f} Km')
print(f'O combustível necessário é de: {combustivel_necessario:.2f} litros')
print(f'O custo total da viagem é de: R$ {custo_total:.2f}')
print(f'O valor por viajante é de: R$ {valor_por_viajante:.2f}')
# ver se o custo da viagem cabe dentro do orçamento
if custo_total > orc:
    valor_faltante = custo_total - orc # calculo do valor que falta para poder fazer a viagem

    print('A viagem \033[31mnão\033[m cabe no orçamento!')
    print(f'O valor que falta para poder fazer a viagem é de: R$ {valor_faltante:.2f}')
else:
    valor_restante = orc - custo_total  # calculo do valor que restou do orçamento'
    print('\033[32mA viagem cabe no orçamento!\033[m')
    print(f'O valor restante é de: R$ {valor_restante:.2f}')
print(f'Código da viagem: {codigo}')
