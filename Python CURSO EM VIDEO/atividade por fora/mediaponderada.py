n1 = float(input('Qual a primeira nota: '))
n2 = float(input('Qual a segunda nota: '))
n3 = float(input('Qual a terceira nota: '))

media_ponderada = ((n1*2) + (n2*3) + (n3*5)) / 10

print(f'Média ponderada é {media_ponderada:.1f}')
