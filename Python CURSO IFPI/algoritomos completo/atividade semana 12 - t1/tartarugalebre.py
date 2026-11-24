def dados():
    vantagem_tartaruga = float(input('Qual a vantagem que a tartaruga tem sobre a lebre: '))
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
    print(f'\n{'TABELA':=^40}')
    print(f'A vantagem da tartaruga é de: {vantagem_tartaruga:.2f} m \nA lebre vai alcançar a tartaruga com o tempo de: {tempo} minutos.\n')
    
if __name__ == '__main__':
    main()