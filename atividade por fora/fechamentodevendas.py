"""fechamento senal de vendas"""
nome = input('Nome do vendedor: ').strip()
meta_diaria = float(input('Qual a meta diária: R$ '))
total_vendas = 0
meta_atingida = 0
maior_venda = 0
dia_da_maior_venda = ''
menor_venda = 0
dia_da_menor_venda = ''
for c in range(1, 8):
    vendas = float(input(f'Venda do dia {c}: R$ '))
    total_vendas += vendas
    if vendas >= meta_diaria:
        meta_atingida += 1
    if c == 1:
        menor_venda = vendas
        dia_da_menor_venda = c
        maior_venda = vendas
        dia_da_maior_venda = c
    if vendas > maior_venda:
        maior_venda = vendas
        dia_da_maior_venda = c
    if vendas < menor_venda:
        menor_venda = vendas
        dia_da_menor_venda = c
# calculos para o programa
meta_semanal = meta_diaria * 7
media = total_vendas / 7
meta_prox90 = meta_semanal * 0.9
# saida para o usuario
print(f"{' Formulário ':=^40}")
print(f'Vendedor: {nome.title()}')  # nome do vendedor
print(f'Meta semanal: R$ {meta_semanal:.2f}')  # meta semanal
print(f'Total vendido: R$ {total_vendas:.2f}')  # total que foi vendido
print(f'Média diária: R$ {media:.2f}')  # media de todas as vendas
# dias que vendeu igual o maior que a meta
print(f'Dias com meta atingida: {meta_atingida}')
# valor e dia da maior venda
print(f'Maior venda: R$ {maior_venda:.2f} — dia {dia_da_maior_venda}')
# valor e dia da menor venda
print(f'Menor venda: R$ {menor_venda:.2f} — dia {dia_da_menor_venda}')
# condições para o programa
if total_vendas >= meta_semanal:
    print('\033[32mMeta senanal atingida!\033[m')
elif meta_prox90 <= total_vendas < meta_semanal:
    print('\033[33mPróximo a meta senanal!\033[m')
elif total_vendas < meta_prox90:
    print('\033[31mMeta semanal não atingida!\033[m')
