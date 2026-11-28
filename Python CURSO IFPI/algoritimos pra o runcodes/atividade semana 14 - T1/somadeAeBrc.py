'''3. Leia duas listas A e B contendo 20 elementos inteiros cada, gerar e exibir uma lista C do mesmo
tamanho cujos elementos sejam a soma dos respectivos elementos de A e B.'''

def receber_dados():
    return int(input(''))

def encher_listas():
    lista_a = []
    lista_b = []
    
    for itens in range(40):
        dados = receber_dados()
        if itens < 20:
            lista_a.append(dados)
        else:
            lista_b.append(dados)
    return lista_a, lista_b

def montar_lista_c(lista_a, lista_b):
    lista_c = []
    for indice in range(20):
        lista_c.append(lista_a[indice] + lista_b[indice])
    return lista_c

def main():
    lista_a, lista_b = encher_listas()
    lista_c = montar_lista_c(lista_a, lista_b)
    print(lista_a)
    print(lista_b)
    print(lista_c)
    
if __name__=='__main__':
    main()