valores = contador = 0
print('''======Digite um número=====
[aperte 0 para encerrar]:''')
while True:
    num = int(input('Número: '))
    if num == 0:
        break
    else:
        valores += num
        contador += 1
print(valores/contador)
    
        