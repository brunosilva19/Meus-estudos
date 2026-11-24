import math

ang = int(input('Digite o ângulo que você deseja: '))

sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tng = math.tan(math.radians(ang))

print(f'O ângulo de {ang} tem SENO de {sen:.2f}. \nO ângulo de {ang} tem COSSENO de {cos:.2f}. \nO ângulo de {ang} tem TANGENTE de {tng:.2f}.')