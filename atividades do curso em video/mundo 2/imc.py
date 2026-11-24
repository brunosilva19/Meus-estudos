"""Programa para medir o imc de uma pessoa e falar que como esta o peso"""
# entrada de dados
altura = float(input('Qual o seu altura: '))
peso = float(input('Qual o seu peso(Kg): '))

# calculo do imc
imc = peso / pow(altura, 2)
# saida pra o usuario
print(
    f'A pessoa que tem {altura:.2f} de altura e pesa {peso}kg tem o IMC de: {imc:.1f} kg/m²')
if imc < 18.5:
    print('Cuidado você está: \033[34mAbaixo do peso\033[m')
elif 18.5 <= imc < 25:
    print('Parabéns você está com:\033[32mPeso ideal\033[m')
elif 25 <= imc < 30:
    print('Cuidado você está com: \033[33mSobrepeso\033[m')
elif 30 <= imc < 40:
    print('MUITO CUIDADO você está com: \033[31mObesidade\033[m')
else:
    print('Você precisa muito ir ao médico: \033[31mObesidade Mórbida\033[m')
