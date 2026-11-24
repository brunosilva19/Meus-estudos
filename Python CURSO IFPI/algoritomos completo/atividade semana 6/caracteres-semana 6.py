def quantidade_de_caracteres(nome):
    x ="".join(nome.split())
    return len(x)

def main():
    nome = input('Qual o seu nome: ').strip()
    resutado = quantidade_de_caracteres(nome)
    print(f'O nome {nome} tem {resutado} letras.')

if __name__ == '__main__':
    main()