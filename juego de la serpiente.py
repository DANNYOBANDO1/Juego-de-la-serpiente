import turtle
import time 
import random

posponer = 0.1

score = 0
high_score = 0

#configuracion de la ventana
wn = turtle.Screen()
wn.title("juego de la serpiente")
wn.bgcolor("black")
wn.setup(width=600,height=600)
wn.tracer(0)

