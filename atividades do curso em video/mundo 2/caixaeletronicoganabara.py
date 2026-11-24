print('=' * 50)
print(f'{"BANCO BBB":^50}')
print('=' * 50)
valor = int(input('Qual valor você quer sacar: R$ '))

ced = 50
total = valor
totalcel = 0

while True:
    
    if total >= ced:
        total -= ced
        totalcel += 1
        
    else:
        if totalcel > 0:
            print(f'Total de {totalcel} cédulas de R$ {ced}')
            
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
            
        totalcel = 0
    
        if total == 0:
            break