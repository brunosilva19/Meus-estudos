mais_18 = homens = mulher_20 = 0
while True:
    print('-' * 40)
    print(f'{"CADASTRE UMA PESSOA":^40}')
    print('-' * 40)
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MF':
        sexo = input('Sexo: [ M / F ]  ').strip().upper()[0]
    if idade > 18:
        mais_18 += 1
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mulher_20 += 1
    ops = ' '
    while ops not in 'SN':
        ops = input('Quer continuar? [S/N] ').strip().upper()[0]
    if ops == 'N':
        break
print('-' * 40)
print(f'Total de pessoas com mais de 18 anos: {mais_18}')
print(f'Ao todo temos {homens} homens cadastrados.')
print(f'E temos {mulher_20} mulheres com menos de 20 anos.')