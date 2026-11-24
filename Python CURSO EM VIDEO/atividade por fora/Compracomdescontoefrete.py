preco_produto = float(input('Preço do produto: R$ '))
quantidade = int(input('Quantidade: '))
desconto = float(input('Desconto: '))
frete = float(input('Frete: R$'))

sub_total = preco_produto * quantidade
desconto_recebido = sub_total * (desconto / 100)
total_compras = (sub_total - desconto_recebido) + frete

print(f'Subtotal: R$ {sub_total:.2f}')
print(f'Desconto recebido: R$ {desconto_recebido:.2f}')
print(f'Total da compra: R$ {total_compras:.2f}')