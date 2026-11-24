def dados():
    vantagem_tartaruga = float(input(''))
    return vantagem_tartaruga

def calcular_tempo(vantagem_tartaruga):
    tempo = lebre = 0
    while lebre < vantagem_tartaruga:
        tempo += 1
        vantagem_tartaruga += 1
        lebre += 10
    return tempo

def main():
    vantagem_tartaruga = dados()
    tempo = calcular_tempo(vantagem_tartaruga)
    print(tempo)

if __name__ == '__main__':
    main()