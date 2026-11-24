maior = 0
for numeros in range(100):
    num = int(input())
    if numeros == 1:
        maior = num
    if num > maior:
        maior = num
print(maior)
    