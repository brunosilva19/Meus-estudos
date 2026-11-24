frase: str = input('Avaliação: ').strip()

print(f'Minúscula: {frase.lower()}')
print(f'Quantidade de caracteres: {len(frase)}')
print(f'Quantidade de letras "e": {frase.lower().count("e")}')
print(f'A palavra "bom" começa na posição: {frase.lower().find("bom")}')
if "excelente" in frase.lower():
    V = "SIM"
    A = "positiva"
else:
    V = "NÃO"
    A = "negativa"
print(f'Possui "excelente"? {V}')
print(f'Avaliação {A}!')
