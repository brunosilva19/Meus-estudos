"""Sistema de cálculo de compra com cupom e frete grátis."""

# Entrada de dados do cliente
nome = input('Produto: ')
preco_uni = float(input('Preço unitário: R$ '))
quantidade = int(input('Quantitade: '))
desconto = int(input('Desconto: '))

# Cabeçalho do cálculo
print('-=-=-=-=-=-=-=-=-=-=-=-=-=-=Calculando Oferta-=-=-=-=-=-=-=-=-=-=-=-=-=-=')

# Cálculo do subtotal e desconto
sub_total = preco_uni * quantidade
valor_des = sub_total * (desconto/100)

# Exibição dos dados do produto
print(f'Produto: {nome.title()}')
print(f'Subtotal: R$ {sub_total:.2f}')
print(f'Desconto: R$ {valor_des:.2f}')

# Cálculo do frete com base no subtotal
if sub_total >= 200:
    FRETE = 0  # Frete grátis para compras acima de R$ 200
    total_compra = sub_total - valor_des
    FRETE_CONCEDIDO = 'Frete grátis concedido!'
else:
    FRETE = 18  # Frete R$ 18 para compras abaixo de R$ 200
    total_compra = sub_total - valor_des + FRETE
    FRETE_CONCEDIDO = 'Frete grátis NÃO concedido!'

# Exibição do valor do frete
print(f'Frete: R$ {FRETE:.2f}')
print(f'Total da compra: R$ {total_compra:.2f}')
print(f'{FRETE_CONCEDIDO}')
