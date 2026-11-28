def receber_dados():
    nome_jogador = input('').strip()
    altura_jogador = float(input(''))

    return nome_jogador, altura_jogador

def encher_lista():
    nomes_jogadores = []
    alturas_jogadores = []

    for contador in range(12):
        nome_jogador, altura_jogador = receber_dados()
        nomes_jogadores.append(nome_jogador)
        alturas_jogadores.append(altura_jogador)

    return nomes_jogadores, alturas_jogadores

def mais_alto(nomes_jogadores, alturas_jogadores):
    maior_altura = alturas_jogadores[0]
    nome_jogador_mais_alto = nomes_jogadores[0]

    for indice in range(1, len(alturas_jogadores)):
        if alturas_jogadores[indice] > maior_altura:
            maior_altura = alturas_jogadores[indice]
            nome_jogador_mais_alto = nomes_jogadores[indice]

    return maior_altura, nome_jogador_mais_alto

def media_de_altura(alturas_jogadores):
    return sum(alturas_jogadores) / len(alturas_jogadores)

def acima_da_media(nomes_jogadores, alturas_jogadores):
    nomes_acima_da_media = []
    alturas_acima_da_media = []
    altura_media = media_de_altura(alturas_jogadores)

    for indice in range(len(alturas_jogadores)):
        if alturas_jogadores[indice] > altura_media:
            nomes_acima_da_media.append(nomes_jogadores[indice])
            alturas_acima_da_media.append(alturas_jogadores[indice])

    return nomes_acima_da_media, alturas_acima_da_media

def imprimir_jogadores_acima_da_media(nomes_acima_da_media, alturas_acima_da_media):
    print('JOGADORES MAIS ALTOS QUE A MÉDIA DO TIME')
    for indice in range(len(nomes_acima_da_media)):
        print(nomes_acima_da_media[indice])
        print(f'{alturas_acima_da_media[indice]:.2f}')

def main():
    nomes_jogadores, alturas_jogadores = encher_lista()
    maior_altura, nome_jogador_mais_alto = mais_alto(nomes_jogadores, alturas_jogadores)
    altura_media = media_de_altura(alturas_jogadores)
    nomes_acima_da_media, alturas_acima_da_media = acima_da_media(nomes_jogadores, alturas_jogadores)
    
    print('JOGADOR MAIS ALTO DO TIME')
    print(nome_jogador_mais_alto)
    print(f'{maior_altura:.2f}')
    print('ALTURA MÉDIA DO TIME')
    print(f'{altura_media:.2f}')
    imprimir_jogadores_acima_da_media(nomes_acima_da_media, alturas_acima_da_media)


if __name__ == '__main__':
    main()