"""Calcula o custo estimado de combustível de uma viagem."""

distancia = float(input('Qual a distância da viagem: '))
consumo = float(input('Consumo do veículo: '))
combustivel = float(input('Valor do combustível: R$ '))

combustivel_necessario = distancia / consumo
valor_do_total = combustivel_necessario * combustivel
print(f'O combustível necessário é de: {combustivel_necessario:.2f} litros')
print(f'O custo dessa viagem é de: R$ {valor_do_total:.2f}')