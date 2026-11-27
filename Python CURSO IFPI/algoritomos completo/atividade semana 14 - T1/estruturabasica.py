'''As estruturas básicas de programação são sequência, condição e repetição. Usando apenas as
estruturas básicas de programação, reescreva as funções abaixo (sem utilizá-las):
a) len(), que recebe uma lista e retorna número de itens;
b) reverse(), que recebe uma lista e retorna uma lista com os itens na ordem invertida;
c) min(),que recebe uma lista e retorna o menor valor
d) max(), que recebe uma lista retorna o maior valor
e) sum(), que recebe uma lista retorna a soma dos valores
Faça a leitura dos valores necessários pelo teclado, a leitura de um número 0 (zero) encerra a
leitura dos elementos da lista. Para cada uma das opções, imprima a lista que foi lida e o
resultado encontrado.
Dica: Você pode usar esses nomes para suas funções: comprimento(), inverter(),
minimo(), maximo(), soma().'''

def receber_dados():
    return int(input('Digite alguns valores[0 para encerrar]: '))

def carregar_lista():
    lista = []
    while True:
        dados = receber_dados()
        if dados == 0:
            break
        lista.append(dados)
    return lista

def comprimento(lista):
    cont = 0
    for intem in lista:
        cont += 1 
    return cont

def inverter(lista):
    return lista[::-1]


def  minimo(lista):
    menor = 0
    for indice,itens in enumerate(lista):
        if indice == 0:
            menor = itens
        elif itens < menor:
            menor = itens
    return menor

def  maximo(lista):
    maior = 0
    for indice,itens in enumerate(lista):
        if indice == 0:
            maior = itens
        elif itens > maior:
            maior = itens
    return maior

def soma(lista):
    soma = 0
    for itens in lista:
        soma += itens
    return soma
    
    
def main():
    lista = carregar_lista()
    len = comprimento(lista)
    contrario = inverter(lista)
    menor = minimo(lista)
    maior = maximo(lista)
    lista_soma = soma(lista)
    print(len)
    print(contrario)
    print(menor)
    print(maior)
    print(lista_soma)
    
if __name__ == '__main__':
    main()