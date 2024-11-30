import turtle
from random import randint, shuffle
from sol import sol
from immeuble import immeuble
# ------------------------------
# ------------------------------
# ------------------------------

def main():
    turtle.setup(800, 600)
    turtle.speed(0)
    # On définit la hauteur du sol
    y_sol = -200
   
    # Dessin du sol de la rue
    sol(y_sol)
    #création du ciel
    turtle.fillcolor('lightblue')
    turtle.pensize(0)
    turtle.begin_fill()
    turtle.up()
    turtle.goto(-400,-200)
    turtle.down()
    turtle.forward(800)
    turtle.left(90)
    turtle.forward(500)
    turtle.left(90)
    turtle.forward(800)
    turtle.left(90)
    turtle.forward(500)
    turtle.left(90)
    turtle.end_fill()
    #création du sol
    turtle.fillcolor('lightgreen')
    turtle.pensize(0)
    turtle.begin_fill()
    turtle.up()
    turtle.goto(-400,-200)
    turtle.down()
    turtle.forward(800)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.forward(800)
    turtle.right(90)
    turtle.forward(200)
    turtle.right(90)
    turtle.end_fill()
    
    # Dessin des immeubles
    for i in range(4):
        immeuble(-320+i*180, y_sol)

    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()
    
if __name__ == '__main__':
    main()



