print('-' * 60)
print(f'{"LOJA DO BRUNO":^60}')
print('-' * 60)
valor_total = valor_maior = mais_barato = count = 0
nome_produto = ' '
while True:
    produto = input('Nome do Produto: ').strip()
    valor = float(input('Preço: R$ '))
    count += 1
    valor_total += valor
    
    if valor > 1000:
        valor_maior += 1
    if count == 1:
        mais_barato = valor
        nome_produto = produto
    if valor < mais_barato:
        mais_barato = valor
        nome_produto = produto
    ops = ' '
    while ops not in 'SN':
        ops = input('Quer continuar? [S/N] ').strip().upper()[0]
    if ops == 'N':
        break
print(f'{"Fim do programa":=^60}')
print(f'O total da compra foi de R$ {valor_total:.2f}')
print(f'Temos {valor_maior}', "produto" if valor_maior == 1 else 'produtos','custando mais de R$ 1000.00')
print(f'O produto mais barato foi : {nome_produto} que custa R$ {mais_barato:.2f}')