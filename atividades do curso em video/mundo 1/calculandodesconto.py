valor = float(input('Qual o preço do produto? R$'))

print(f'O produto que custava R${valor:.2f}, na promoção com desconto de 5% vai custar R${valor - (valor * 0.05):.2f}.')
