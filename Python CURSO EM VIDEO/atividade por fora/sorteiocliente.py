from random import randint

quantidade_de_pessoas = int(input('Quantidade de participantes: '))

sorteio_cliente = randint(1, quantidade_de_pessoas)
sorteio_codigo = randint(1000, 9999)

print(f'Participante sorteado: {sorteio_cliente}')
print(f'Código de confirmação: {sorteio_codigo}')
