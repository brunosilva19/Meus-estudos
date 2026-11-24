def calcular_tempo(segundos):
    horas = segundos // 3600
    min = (segundos % 3600) // 60
    sec = segundos % 60
    x = (f'{horas:2d}:{min:2d}:{sec:2d}')
    return x 
def main():
    valor = int(input('Digite um tempo em segundos: '))
    tempo = calcular_tempo(valor)
    print(tempo)
if __name__ == '__main__':
    main()
