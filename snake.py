"""Snake, classic arcade game.

Exercises

1. How do you make the snake faster or slower?
2. How can you make the snake go around the edges?
3. How would you move the food?
4. Change the snake to respond to arrow keys.

"""

from turtle import *
from random import randrange
from freegames import square, vector

food = vector(0, 0)
snake = [vector(10, 0)]
aim = vector(0, -10)

i = randrange(0,4)
if i == 0:
    color = "green"
    colorC = "brown"
elif i == 1:
    color = "brown"
    colorC = "blue"
elif i == 2:
    color = "blue"
    colorC = "yellow"
elif i == 3:
    color = "yellow"
    colorC = "black"
elif i == 4:
    color = "black"
    color = "green"


def change(x, y):
    "Change snake direction."
    aim.x = x
    aim.y = y

def inside(head):
    "Return True if head inside boundaries."
    return -200 < head.x < 190 and -200 < head.y < 190

def move():
    "Move snake forward one segment." "Como funciona?"
    write('Andres A00829535', move = True, align = 'right', font = ('Arial', 14, 'normal'))

    head = snake[-1].copy()
    head.move(aim)

    if not inside(head):
        if head.x == 190:
            head.x = -200
        elif head.x == -200:
            head.x = 190
        elif head.y == 190:
            head.y = -200
        elif head.y == -200:
            head.y = 190
    if head in snake:
        square(head.x, head.y, 9, 'red')
        update()
        return

    snake.append(head)

    if head == food:
        print('Snake:', len(snake))
        food.x = randrange(-15, 15) * 10
        food.y = randrange(-15, 15) * 10
        # añadir instrucciones par que de forma aleatoria
        # cambiar de color
        # color = 'blue'
        # colorC = 'cyan'
    else:
        snake.pop(0)
        # mover aleatoriamente la comida
        # food.move(movimientos_food[randrange(0, 4)])
        
        # if not inside (food) or food in snake:
            # square(food.x, food.y, 9, 'red')
            # update()
            # return

    clear()

    for body in snake:
        "Color"
        square(body.x, body.y, 9, color)

    square(food.x, food.y, 9, colorC)
    update()
    ontimer(move, 100)

setup(420, 420, 0, 0)
hideturtle()
tracer(False)
listen()
onkey(lambda: change(10, 0), 'Right')
onkey(lambda: change(-10, 0), 'Left')
onkey(lambda: change(0, 10), 'Up')
onkey(lambda: change(0, -10), 'Down')
move()
done()