# alugue_de_carro
dias = int(input('Quantos dias você alugou o carro? '))
km = float(input('Quantos KM rodado? '))

vda = (60 * dias) + (0.15 * km)

print(f'O total a pagar é de R${vda:.2f}!')
