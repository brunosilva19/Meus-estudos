placa = input('Qual o número da placa: ').strip()

print(f'Placa padronizada: {placa.upper()}')
print(f'Quantidade de caracteres: {len(placa)}')
print(f'Letras iniciais: {placa[0:3].upper()}')
print(f'Primeiro número: {placa[3:4]}')
print(f'Letra central: {placa[4:5].upper()}')
print(f'Números finais: {placa[-2:]}')
if (
    len(placa) == 7
    and placa[0:3].isalpha()
    and placa[3].isnumeric()
    and placa[4].isalpha()
    and placa[-2:].isnumeric()
):
    print('Placa válida!')
else:
    print('Placa inválida!')
