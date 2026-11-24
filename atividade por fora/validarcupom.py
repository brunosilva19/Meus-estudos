cupom = input('Código promocional: ').strip().upper()
caracteres = len(cupom)
prefixo = 'PROMO' in cupom[:5]
numero = cupom[-4:].isnumeric()
print(f'Código padronizado: {cupom}')
print(f'Tipo primitivo: {type(cupom)}')
print(f'Quantidade de caracteres: {caracteres}')
print(f'Prefixo: {cupom[:5]}')
print(f'Números finais: {cupom[-4:]}')
if prefixo and numero and caracteres == 9:
    print('Código válido!')
else:
    print('Código invalido!')
