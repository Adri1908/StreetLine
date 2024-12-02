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
    # Positionne la tortue
    turtle.up()
    turtle.goto(x, y)
    turtle.down()

    # Prépare le remplissage
    turtle.fillcolor("white")  # Définit la couleur de remplissage à blanc
    turtle.begin_fill()        # Commence le remplissage

    # Dessine le carré
    for i in range(4):
        turtle.forward(30)  # Avance de 30 unités
        turtle.left(90)     # Tourne à gauche de 90 degrés

    turtle.end_fill()        # Termine le remplissage

if __name__ == '__main__':
    fenetre(0,0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()
