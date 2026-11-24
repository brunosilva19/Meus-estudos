valores = contador = 0
while True:
    num = int(input(''))
    if num == 0:
        break
    else:
        valores += num
        contador += 1
print(f'{valores/contador:.2f}')
    
        