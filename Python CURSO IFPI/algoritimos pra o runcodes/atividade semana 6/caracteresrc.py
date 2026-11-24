def quantidade_de_caracteres(nome):
    x ="".join(nome.split())
    return len(x)

def main():
    nome = input('').strip()
    resutado = quantidade_de_caracteres(nome)
    print(f'{resutado}')

if __name__ == '__main__':
    main()