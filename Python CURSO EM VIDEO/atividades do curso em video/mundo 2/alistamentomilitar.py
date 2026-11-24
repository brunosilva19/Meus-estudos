"""Módulo para cálculo de alistamento militar."""
from datetime import datetime

# entrada de dados
ano_usuario = int(input('Qual o ano do seu nascimento: '))

# ano atula e idade do usuario
ANO_ATUAL = datetime.today().year
idade_usuario = ANO_ATUAL - ano_usuario

# saida pra o usuario
print('===============================INFORMAÇÕES===============================')
print(f'Quem nasceu em {ano_usuario} tem {idade_usuario} ano(s) em {ANO_ATUAL}!')
# condições para o alistamento
if idade_usuario < 18:
    tempo_para_alistamento = 18 - idade_usuario
    ano_alistamento = ANO_ATUAL + tempo_para_alistamento
    print(f'Ainda falta {tempo_para_alistamento} ano(s) para o Alistamento!')
    print(f'Seu alistamento será em: {ano_alistamento}')
elif idade_usuario == 18:
    print('Você está na idade certa para o alistamento, compareça à companhia!')
elif idade_usuario > 18:
    tempo_para_alistamento = idade_usuario - 18
    ano_alistamento = ANO_ATUAL - tempo_para_alistamento
    print(f'Já se passaram {tempo_para_alistamento} ano(s) do seu alistamento!\nQue era no ano de {ano_alistamento}.')
