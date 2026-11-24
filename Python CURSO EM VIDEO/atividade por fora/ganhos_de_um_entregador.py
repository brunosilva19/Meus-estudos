quantidade_entrega = int(input('Quantas entregas você fez? '))
valor_entrega = float(input('Valor por entrega? R$ '))
gorjeta = float(input('Total de gorjeta? R$ '))

entrega_total = quantidade_entrega * valor_entrega
total = entrega_total + gorjeta

print(f'O valor das entregas: R${entrega_total:.2f} \nGanho total: R$ {total:.2f}')