from random import choice # aqui importa a função choice da bibliotema random

#aqui é as palavra que tem diponivel pra ser usadas no jogo
palavra = ["banana", "pera", "casa", "paralelepipedo", "computador", "abacaxi", "parlamento", "curso", "macaco", "monitor"] 

palavra_sorteada = choice(palavra).upper() # aqui escolhe a palavra de dentro da lista


palavra_sorteada_escondida = [] # aqui vai ser onde o for letras vai quarda as _ para cada letra a palavra

letras_digitadas = []

for letra in palavra_sorteada:
    palavra_sorteada_escondida.append('_')

vida = ["❤︎","❤︎","❤︎","❤︎","❤︎"]

tentativas = 5

quantidade_de_letras_restantes = 0 # quantidades de letas restantes


print('\033[32m⫘⫘⫘⫘⫘⫘\033[m' * 11)
print("""               Vamos jogar um jogo da forca!!!
Eu pensei em um palavra e quero que voce tente advinha qual é!""")
print('\033[32m⫘⫘⫘⫘⫘⫘\033[m' * 11)

while tentativas > 0:
    # isso tem que se repetir sempre
    
    while True:
        print(f'Vida: \033[31m{'  '.join(vida)}\033[m')
        print(f'letras digitadas: {','.join(letras_digitadas) if letras_digitadas else  'Nenhuma'}')
        print(f'PALAVRA: {''.join(palavra_sorteada_escondida)}')
        print('\033[32m⫘⫘⫘⫘⫘⫘\033[m' * 11)
        usuario = input('Digite uma letra: ').strip().upper()

        if len(usuario) != 1 or not usuario.isalpha():
            print('\033[31mDigite apenas uma letra válida!\033[m')
            continue

        if usuario in letras_digitadas:
            print('\033[34mVocê já tentou essa letra!\033[m')
            continue
        break
    
    letras_digitadas.append(usuario)
    
    if usuario not in palavra_sorteada:
        print(f'\033[31mNão tem a letra {usuario} nessa palavra\033[m')
        tentativas -= 1
        vida.pop() 
          
    for indice, letras in enumerate(palavra_sorteada):
        if usuario == letras:
            palavra_sorteada_escondida[indice] = usuario 
        
    for c in palavra_sorteada_escondida:
        if c == '_':
            quantidade_de_letras_restantes += 1
            
    print('\033[32m⫘⫘⫘⫘⫘⫘\033[m' * 11)
    
    if ''.join(palavra_sorteada_escondida) == palavra_sorteada:
            print('\033[32mPARABÉNS, VOCÊ DESCOBRIU A PALAVRA\033[m')
            break
        
    if quantidade_de_letras_restantes <= 3 and tentativas > 0:
        
        print(f'Vida: \033[31m{'  '.join(vida)}\033[m')
        print(f'letras digitadas: {','.join(letras_digitadas) if letras_digitadas else 'Nenhuma'}')
        print(f'PALAVRA: {''.join(palavra_sorteada_escondida)}')
        usuario = input('\033[35mTente adivinha a palavra:[ou aperte enter para continuar]:\033[m').strip().upper()
        print('\033[32m⫘⫘⫘⫘⫘⫘\033[m' * 11)
        if usuario:
            if usuario != palavra_sorteada:
                print(f'\033[31mA palavra não é {usuario}!\033[m')
                tentativas -= 1
                vida.pop()
            else:
                print('\033[32mPARABÉNS, VOCÊ DESCOBRIU A PALAVRA\033[m')
                break
            
    quantidade_de_letras_restantes = 0
    
if tentativas == 0:
    print('\033[32m⫘⫘⫘⫘⫘⫘\033[m' * 11)
    print('\033[31mVocê perdeu!\033[m')
    print(f'A palavra era: {palavra_sorteada}')
    print('\033[32m⫘⫘⫘⫘⫘⫘\033[m' * 11)