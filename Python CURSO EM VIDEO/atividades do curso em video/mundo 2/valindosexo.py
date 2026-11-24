sexo = input('Informe seu sexo [M/F]: ').strip().upper()[0]
while sexo not in ('M', 'F'):
    sexo = input('Dados inválidos. Informe seu sexo [M/F]: ').strip().upper()[0]
print(f'Sexo {sexo} resgistrado com sucesso!')