from math import ceil
quantidade_produto = int(input('Quantidade de produto: '))
capacidade_caixa = int(input('Capacidade de cada caixa: '))

cxt = quantidade_produto // capacidade_caixa
pr = quantidade_produto % capacidade_caixa
tcn = ceil(quantidade_produto / capacidade_caixa)
print(f'Caixas completamente cheias: {cxt} \nProdutos restantes: {pr} \nTotal de caixas necessárias: {tcn}')