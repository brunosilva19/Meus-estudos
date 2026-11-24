# entradas de informação
nome_vendedor = input('Vendedor: ').strip()
salario = float(input('Salário fixo: R$ '))
total_vendas = float(input('Total vendido: R$ '))
meta = float(input('Meta de vendas: R$ '))
# calculos para o programa
comissao = total_vendas * 0.05
bonus = 0
# condição para bonus
if total_vendas >= meta:
    bonus = 300
    META_TEXT = "\033[32mMeta atingida!\033[m"
    valor = total_vendas - meta
    text = f"Valor a cima da meta: R$ {valor:.2f}"
else:
    META_TEXT = "\033[31mMeta não atingida!\033[m"
    valor = meta - total_vendas
    text = f"Valor para atingir a meta: R$ {valor:.2f}"
pagamento_total = salario + comissao + bonus
# saida pra o usuario
print(f'{"QUADRO DE METAS":=^40}')
print(f'Vendedor(a): {nome_vendedor.title()}')
print(f'Comissão: R$ {comissao:.2f}')
print(f'Bônus: R$ {bonus:.2f}')
print(f'Pagamento total: R$ {pagamento_total:.2f}')
print(META_TEXT)
print(text)
