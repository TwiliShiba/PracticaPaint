from turtle import *
from freegames import vector
import math

def line(start, end):
    "Draw line from start to end."
    "Crea una línea desde el punto de inicio hasta el punto final"
    up()
    goto(start.x, start.y)
    down()
    goto(end.x, end.y)

def square(start, end):
    "Draw square from start to end."
    "Crea un cuadrado con una esquina inferior izquierda en el punto de inicio"
    "con con una esquina inferior derecha en el punto final"
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    "Ciclo para repetir el movimiento hacia delante y la rotación de 90° a la izquierda cuatro veces"
    for count in range(4):
        forward(end.x - start.x)
        left(90)

    end_fill()

def circ(start, end):
    "Draw circle from start to end."
    "Crea un círculo con un centro en el punto de inicio y un radio en punto final"
    
    "Variable que calcula la distancia entre punto de inicio (centro) y"
    "el radio en punto final"
    rad = math.sqrt((end.x - start.x)**2 + (end.y - start.y)**2)
    "Variable que guarda el centro del círculo"
    center = start.y - rad
    
    up()
    goto(start.x, center)
    down()
    begin_fill()
    "Dibujar el círculo"
    circle(rad)

    end_fill()

def rectangle(start, end):
    "Draw rectangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()
    
    "Ciclo para repetir el movimiento hacia delante, la rotación de 90° a la izquierda,"
    "el movimiento hacia delante dos veces menos que el lado horizontal y otra rotación"
    "de 90° a la izquierda 2 veces"
    for count in range(2):
        forward(end.x - start.x)
        left(90)
        forward((end.x - start.x) / 2)
        left(90)

    end_fill()

def triangle(start, end):
    "Draw triangle from start to end."
    up()
    goto(start.x, start.y)
    down()
    begin_fill()

    "Ciclo para repetir el movimiento hacia delante y la rotación de 120° a la izquierda tres veces"
    for count in range(3):
        forward(end.x - start.x)
        left(120)

    end_fill()

def tap(x, y):
    "Store starting point or draw shape."
    start = state['start']

    if start is None:
        state['start'] = vector(x, y)
    else:
        shape = state['shape']
        end = vector(x, y)
        shape(start, end)
        state['start'] = None

def store(key, value):
    "Store value in state at key."
    state[key] = value

state = {'start': None, 'shape': line}
setup(420, 420, 370, 0)
onscreenclick(tap)
listen()
onkey(undo, 'u')
onkey(lambda: color('black'), 'K')
onkey(lambda: color('white'), 'W')
onkey(lambda: color('green'), 'G')
onkey(lambda: color('blue'), 'B')
onkey(lambda: color('red'), 'R')
onkey(lambda: color('yellow'), 'Y')
onkey(lambda: store('shape', line), 'l')
onkey(lambda: store('shape', square), 's')
onkey(lambda: store('shape', circ), 'c')
onkey(lambda: store('shape', rectangle), 'r')
onkey(lambda: store('shape', triangle), 't')
done()