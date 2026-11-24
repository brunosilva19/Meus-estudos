def entrada_de_dados():
    idade = int(input(''))
    return idade

def tratamento_de_dados():
    numero_de_pessoas = 0
    soma_idades = 0
    menor_idade = 0
    maior_idade = 0
    while True:
        idade = entrada_de_dados()
        if idade == 0:
            break
        numero_de_pessoas += 1
        soma_idades += idade
        if numero_de_pessoas == 1:
            menor_idade = idade
            maior_idade = idade
        if idade > maior_idade:
            maior_idade = idade
        if idade < menor_idade:
            menor_idade = idade
    return numero_de_pessoas, soma_idades, menor_idade, maior_idade
    
def resultados(numero_de_pessoas, soma_idades, menor_idade, maior_idade):
    print(f'{numero_de_pessoas}')
    print(f'{soma_idades/numero_de_pessoas:.2f}')
    print(f'{menor_idade}')
    print(f'{maior_idade}')
    
def main():
    numero_de_pessoas, soma_idades, menor_idade, maior_idade = tratamento_de_dados()
    resultados(numero_de_pessoas, soma_idades, menor_idade, maior_idade)

if __name__ == '__main__':
    main()
