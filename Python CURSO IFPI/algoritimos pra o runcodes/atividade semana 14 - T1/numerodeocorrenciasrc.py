'''Usando apenas as estruturas básicas de programação, reescreva a funções count(), que recebe
uma lista e um valor e retorna o número de ocorrências do valor na lista. Por exemplo
count([1, 2, 3, 2, 4, 2, 5], 2) retorna 3, a quantidade de vezes que o valor 2
aparece na lista.
Faça a leitura pelo teclado, a leitura de um 0 (zero) encerra a leitura. Primeiro leia a lista e depois
o valor para pesquisar. Imprima a lista que foi lida, o valor pesquisado e o resultado encontrado.'''

def receber_dados():
    return int(input(''))

def valor_numero():
    return int(input(''))

def criar_lista():
    lista = []
    while True:
        dados = receber_dados()
        if dados == 0:
            break
        lista.append(dados)
    return lista

def contador_vezes(lista, valor):
    quantidade = 0
    for item in (lista):
        if item == valor:
            quantidade += 1
    return quantidade


def main():
    lista = criar_lista()
    valor = valor_numero()
    quantidade = contador_vezes(lista, valor)
    print(lista)
    print(valor)
    print(quantidade)
    
if __name__=='__main__':
    main()