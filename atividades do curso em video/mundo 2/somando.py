saida = soma = quantidade = 0

while saida != 999:
    saida = int(input('Digite um número [999 para parar]: '))
    
    if saida != 999:
        soma += saida
        quantidade += 1
        
print(f'Você digitou {quantidade} números e a soma entre eles foi {soma}.')