"""códigos de Encomenda"""
codigo_validado = []
count_valido = 0
count_invalido = 0
for c in range(0, 5):
    codigo = input(f'Código {c + 1}: ').strip().upper()
    # validar codigo
    if len(codigo) == 8 and codigo[:3].isalpha() and codigo[3] == '-' and codigo[-4:].isnumeric():
        codigo_validado.append([codigo, 'Válido'])
        count_valido += 1
    else:
        codigo_validado.append([codigo, 'Inválido'])
        count_invalido += 1
print(f'{' Formulário ':=^40}')
for x in range(0, 5):
    print(f'{codigo_validado[x][0]} — {codigo_validado[x][1]}')
print(f'Código válido: {count_valido}')
print(f'Código inválido: {count_invalido}')
