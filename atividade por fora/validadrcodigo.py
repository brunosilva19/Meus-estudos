""" Validar codigo de reserva"""

# entrada de dado
codigo = input('Código da reserva: ').strip()

quantidade_de_caracteres = len(codigo)
prefixo_trv = codigo[:3]
ano = codigo[4:8]
estado = codigo[-2:]

# teste do codigo
test1 = quantidade_de_caracteres == 11
test2 = prefixo_trv.isalpha()
test3 = ano.isnumeric()
test4 = estado.isalpha()

separadores_corretos = (
    codigo[3:4] == '-'
    and codigo[8:9] == '-'
)

# sairda pra o usuario

print(f'Código padronizado: {codigo.upper()}')
print(f'Quantidade de caracteres: {quantidade_de_caracteres}')
print(f'Prefixo: {prefixo_trv.upper()}')
print(f'Ano: {ano}')
print(f'Estado: {estado.upper()}')
print(f'Separadores corretos? {separadores_corretos}')

if test1 and test2 and test3 and test4 and separadores_corretos:
    print('\033[32mCódigo válido!\033[m')
else:
    print('\033[31mCódigo inválido!\033[m')
