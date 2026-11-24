# entrada de dados

altura = float(input('Digite a altura da parede: '))
comprimento = float(input('Digite o comprimento da parede: '))
largura = float(input('Digite a largura da parede: '))

# calculos para o programa

area_piso = comprimento * largura
volume = comprimento * altura * largura
area_das_paredes = 2 * altura * largura + 2 * altura * comprimento

#saida para o usuario

print(f'A área do piso é de: {area_piso}m²')
print(f'O volume da sala em metros cúbicos é de: {volume}m³')
print(f'A área das paredes é de: {area_das_paredes}m²')
