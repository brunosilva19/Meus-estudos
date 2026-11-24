print('=' * 50)
print(f'{"BANCO BBB":^50}')
print('=' * 50)
valor = int(input('Qual valor você quer sacar: R$ '))

cont_50 = cont_20 = cont_10 = cont_1 = 0

while valor != 0:
    
    if valor >= 50:
        valor -= 50
        cont_50 += 1
        
    elif valor >= 20:
        valor -= 20
        cont_20 += 1
        
    elif valor >= 10:
        valor -= 10
        cont_10 += 1
        
    else:
        valor -= 1
        cont_1 += 1
    
    
print('=' * 50)
if cont_50 != 0:
    print(f'Total de {cont_50} cédulas de R$ 50.00')
if cont_20 != 0:
    print(f'Total de {cont_20} cédulas de R$ 20.00')
if cont_10 != 0:
    print(f'Total de {cont_10} cédulas de R$ 10.00')
if cont_1 != 0:
    print(f'Total de {cont_1} cédulas de R$ 1.00')
print('=' * 50)
print('Volte sempre ao BANCO BBB! Tenha um Bom dia!')