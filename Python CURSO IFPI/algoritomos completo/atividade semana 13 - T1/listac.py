lista_a = []
lista_b =  []
lista_c = []
    
for c in range(50):
    num = int(input(f'Digite o {c + 1}º número: '))
    if c < 25:
        lista_a.append(num)
    else:
        lista_b.append(num)
        

for numero in range(25):
    lista_c.append(lista_a[numero])
    lista_c.append(lista_b[numero])
    
print('lista A: ',lista_a)
print('lista B: ',lista_b)    
print('lista C: ',lista_c)