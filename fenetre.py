from rectangle import rectangle
import turtle

def fenetre(x,y):
    '''
    Paramètres :
        x est l'abcisse du centre de la fenêtre
        y est l'ordonnée du sol du niveau de la fenetre
    Remarque:
        dessine une fenetre de 30 pixels sur 30 pixels

    '''
<<<<<<< HEAD
    turtle.up()
    turtle.goto(x, y)
    turtle.down()
    turtle.forward(30)  # Forward turtle by 100 units
    turtle.left(90)  # Turn turtle by 90 degree
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.forward(30)
    turtle.left(90)
    turtle.up()
    turtle.forward(15)
    turtle.down()
    turtle.left(90)
    turtle.forward(30)
    turtle.up()
    turtle.left(90)
    turtle.forward(15)
    turtle.left(90)
    turtle.forward(15)
    turtle.down()
    turtle.left(90)
    turtle.forward(30)
=======
    
    t = turtle.Turtle()
    t.up()
    t.goto(x, y)
    t.down()
    t.forward(30)  # Forward turtle by 100 units
    t.left(90)  # Turn turtle by 90 degree
    t.forward(30)
    t.left(90)
    t.forward(30)
    t.left(90)
    t.forward(30)
    t.left(90)
    t.up()
    t.forward(15)
    t.down()
    t.left(90)
    t.forward(30)
    t.up()
    t.left(90)
    t.forward(15)
    t.left(90)
    t.forward(15)
    t.down()
    t.left(90)
    t.forward(30)

>>>>>>> 25c6a1497c60ffb318256954f1684baabd54d3e0
if __name__ == '__main__':
    fenetre(0,0)
    # On ferme la fenêtre s'il y a un clique gauche
    print("Hello thomas")
    turtle.exitonclick()
