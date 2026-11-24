"""Programa para saber qual a classe de a cordo com idade"""
from datetime import date
ano_atual = date.today().year
#entrada de dados
ano_nascimento = int(input('Qual o seu ano de nascimento: '))
#calculo para saber a idade do atleta
idade = ano_atual - ano_nascimento
#saida para o usuario
print(f"Quem nasceu em {ano_nascimento} tem {idade} anos no ano de {ano_atual}")
#condições para a classificação
if idade <= 9:
    print("Sua categoria é MIRIM!")
elif idade <= 14:
    print("Sua categoria é INFANTIL")
elif idade <= 19:
    print("Sua categoria é JÚNIOR")
elif idade <= 25:
    print("Sua categoria é SÊNIOR")
elif idade > 25:
    print("Sua categoria é MASTER")
