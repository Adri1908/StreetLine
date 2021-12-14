from turtle import *
import turtle
from rectangle import rectangle
from trait import trait

def fenetre_balcon(x,y):
    '''
    Paramètres :
        x est l'abcisse du centre de la porte-fenetre-balcon
        y est l'ordonnée du sol du niveau de la porte-fenetre-balcon
    Remarque:
        Dessine une porte-fenetre avec balcon en 2 temps: la porte fenetre de 30 pixels de large par 50 pixels de hauteur
        puis le balcon
    '''
    # porte-fenetre
    color('black', 'lightgrey')
    begin_fill()
    for i in range (2):
        forward(30)
        right(90)
        forward(50)
        right(90)
    end_fill()
    up()

    # balcon
    turtle.pensize(3)
    right(90)
    forward(25)
    right(90)
    forward(5)
    right(180)
    down()
    for i in range(2):
        forward(40)
        right(90)
        forward(25)
        right(90)
    
    for i in range(3):
        forward(5)
        right(90)
        forward(25)
        left(90)
        forward(5)
        left(90)
        forward(25)
        right(90)
    forward(5)
    right(90)
    forward(25)

if __name__ == '__main__':
    fenetre_balcon(0,0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()