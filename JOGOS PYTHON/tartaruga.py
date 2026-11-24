from turtle import *
from random import randint

speed(0)
bgcolor("midnight blue")
hideturtle()
color("white")

# desenhar a lua
penup()
goto(180, 150)
dot(80, "lightyellow")

# função da estrelinha simples
def estrela():
    for i in range(4):
        forward(10)
        backward(20)
        forward(10)
        left(45)

# desenhar 10 estrelas em posições aleatórias
for i in range(20):
    penup()
    goto(randint(-450, 450), randint(-380, 380))
    pendown()
    estrela()

done()