fatia = int(input('Quantas fatias a pizza tem: '))
amigos = int(input('Quantas pessoas são ao todo: '))
divisao = fatia // amigos
pedaco_que_sobra = fatia % amigos
print(f'Cada um recebeu {divisao} fatia(s) e sobrou {pedaco_que_sobra} tatia(s).')