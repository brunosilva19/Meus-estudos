valor_carro = float(input(''))
banco = 10000
meses = 0
while banco <= valor_carro:
    meses += 1
    banco += (banco * 0.007)
    valor_carro += (valor_carro * 0.004)
print(meses)