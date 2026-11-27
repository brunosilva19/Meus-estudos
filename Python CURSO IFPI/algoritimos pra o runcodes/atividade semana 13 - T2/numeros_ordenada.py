def criar_lista_ordenada():
    return [], []


def colocar_na_lista(lista):
    for _ in range(100):
        valor = int(input('Digite um valor: '))
        lista.append(valor)
    lista.sort()


def calculos(lista_ordenada, lista_alterada):
    for indice, numeros in enumerate(lista_ordenada):
        if indice % 2 == 0:
            lista_alterada.append(numeros * 3)
        else:
            lista_alterada.append(numeros * 5)
        
         
def main():
    lista_ordenada, lista_alterada = criar_lista_ordenada()
    colocar_na_lista(lista_ordenada)
    calculos(lista_ordenada, lista_alterada)
    print(lista_alterada)
    
if __name__ == '__main__':
    main()