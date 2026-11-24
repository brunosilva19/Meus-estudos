# Meta diária de água
nome = input('Qual o seu nome: ').strip()
peso = float(input('Qual o seu peso(kg): '))
agua_bebida = float(input('Quantidade de água consumida(L): '))
# calculo para o programa
meta = (peso * 35)/1000
# saidas para o usuário
print(f'{'Meta de Água':=^40}')
print(f'Nome: {nome.title()}')
print(f'Meta diária: {meta:.2f} litros')
print(f'Água consumida: {agua_bebida:.2f} litros')
# condição para bate a meta
if agua_bebida < meta:
    print('\033[31mMeta ainda não atingida!\033[m')
    quantidade_faltante = meta - agua_bebida
    print(
        f'Quantidade que falta para atingir a meta é: {quantidade_faltante:.2f} litros')
else:
    print('\033[32mMeta atingida!\033[m')
    quantidade_acima = agua_bebida - meta
    print(f'Você bebeu {quantidade_acima:.2f} litros acima da meta.')
