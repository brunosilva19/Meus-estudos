""""soma de todos os multiplos de 3 no intervalor de 1 a 500"""
soma = 0
quantida = 0
for multiplo in range(1, 501, 2):
    if multiplo % 3 == 0:
        soma += multiplo
        quantida += 1
print(f'A soma ente {quantida} valores pedido é de {soma}')