nome = input('Funcionário: ').strip()
horas_trabalho = int(input('Horas trabalhadas: '))
valor_por_hora = float(input('Valor por hora: R$ '))
# calcailar a quantidade das 40 horas
print(f'Nome: {nome.capitalize()}')
print(f"Primeiro nome: {nome.split()[0].capitalize()}")
if horas_trabalho <= 40:
    horas_normal = horas_trabalho
    pagamento_normal = horas_trabalho * valor_por_hora
    pagamento_hora_extra = 0
    EXTRA = 0
    TEXT = "Não possui"
    total_pagamento = pagamento_hora_extra + pagamento_normal
else:
    pagamento_normal = 40 * valor_por_hora
    horas_normal = 40
    EXTRA = horas_trabalho - 40
    pagamento_hora_extra = EXTRA * (valor_por_hora + valor_por_hora * 0.5)
    TEXT = "Possui"
    total_pagamento = pagamento_normal + pagamento_hora_extra
print(f'Horas normais: {horas_normal}')
print(f'horas extra: {EXTRA}')
print(f'Pagamento normal: R$ {pagamento_normal:.2f}')
print(f'Pagamento das horas extra: R$ {pagamento_hora_extra:.2f}')
print(f'Pagamento total: R$ {total_pagamento:.2f} ')
print(f'{TEXT} horas extras!')


