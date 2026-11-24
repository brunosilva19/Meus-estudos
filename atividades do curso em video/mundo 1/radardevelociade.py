velociade = float(input('Qual é a velociade atual do carro? '))
if velociade <= 80:
    print('Tenha um bom dia! Dirija com segurança!')
else:
    multa = (velociade - 80) * 7
    print(f'MULTADO! Você excedeu o limite permitido que é de 80km/h \nVocê deve pagar uma multa de R$ {multa:.2f}')
