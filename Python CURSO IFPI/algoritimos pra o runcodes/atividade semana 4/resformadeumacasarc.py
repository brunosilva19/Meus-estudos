#entrada de dados
altura = float(input(''))
comprimento = float(input(''))
largura = float(input(''))
#calculos para o programa
area_piso = int(comprimento * largura)
volume = int(comprimento * altura * largura)
area_das_paredes = int(2 * altura * largura + 2 * altura * comprimento)

print(f'{area_piso}\n{volume}\n{area_das_paredes}')