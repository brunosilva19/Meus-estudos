def lista_notas():
    return [], []

def notas(lista_notas):
    for _ in range(50):
        lista_notas.append(float(input('Escreva a nota do aluno: ')))

def notas_maior(lista_notas, lista_maior):
    for indice, notas in enumerate(lista_notas):
        if notas >= 6:
            lista_maior.append(indice)

def main():
    lista_nota, lista_maior = lista_notas()
    notas(lista_nota)
    notas_maior(lista_nota,lista_maior)
    print(lista_maior)

if __name__ == '__main__':
    main()