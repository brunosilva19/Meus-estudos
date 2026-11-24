num = int(input(''))
count = 2
valor = 1
while count <= num:
    valor += ( 1 / count)
    count += 1
print(f'{valor:.4f}')