saida = ' '
maior = menor = media = cont = 0
while saida != 'N':
    
    num = int(input('Digite um número: '))
    saida = input('Quer continuar? [S/N]').strip().upper()[0]
    media += num
    if cont == 0:
        maior = num
        menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    cont += 1
print(f'Você digitou {cont} números e a média foi de {media/cont:.2f}')     
print(f'O maior valor foi {maior} e o menor valor foi {menor}')