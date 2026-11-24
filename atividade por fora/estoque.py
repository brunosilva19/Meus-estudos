# entra de informação

nome_do_produto = input('Produto: ').strip()
estoque = int(input('Estoque atual: '))
vendas = int(input('Vendas por dia: '))
dias = int(input('Dias até a a proxima entrega: '))
# calculos para rodar o programa

demanda_prevista = vendas * dias

# saida pra o usuário
print(f'Produto: {nome_do_produto.title()}')
print(f'Demanda prevista: {demanda_prevista} unidades')

if demanda_prevista > estoque:
    print('\033[31mEstoque insuficiente!\033[m')
    print(f'Quantidade faltante: {demanda_prevista - estoque} unidade(s)')
else:
    print('\033[32mEstoque suficiente!\033[m')
    print(f'Quantidade restante: {estoque - demanda_prevista} unidade(s)')
