import turtle

def porte2(x,y,couleur):
    '''
    Paramètres :
        x est l'abcisse du centre de la porte
        y est l'ordonnée du sol du niveau de la porte
        couleur : couleur de la porte
    remarque:
        Cette fonction dessine une porte dont le haut est un demi cercle
        La porte a une largeur totale de 30 pixels
        La partie rectangulaire a une hauteur de 40 pixels
        La partie semi circulaire a un rayon de 15 pixels
    '''
    
    # Dessiner le rectangle
    turtle.up()
    turtle.goto(x, y)  # Bas-gauche du rectangle
    turtle.fillcolor(couleur)  # Définit la couleur de remplissage pour le demi-cercle
    turtle.begin_fill()  # Commence le remplissage
    turtle.down()
    
    for i in range(2):  # Deux côtés longs et deux côtés courts
        turtle.forward(30)  # Largeur du rectangle
        turtle.left(90)
        turtle.forward(40)  # Hauteur du rectangle
        turtle.left(90)
    turtle.end_fill()  # Termine le remplissage
    
    # Dessine la partie semi-circulaire
    turtle.begin_fill()  # Commence le remplissage

    # Positionner pour dessiner le demi-cercle
    turtle.up()
    turtle.goto(x+30, y + 40)  # Se place au centre supérieur du rectangle
    turtle.down()

    # Demi-cercle
    turtle.setheading(90)  # Oriente la tortue vers le haut
    turtle.circle(15, 180)  # Dessine un demi-cercle de rayon 15
    turtle.end_fill()  # Termine le remplissage
    
    turtle.setheading(0) # Rétablie l'orientation de la tortue

if __name__ == '__main__':
    porte2(0, 0, "red")
    # On ferme la fenêtre s'il y a un clic gauche
    turtle.exitonclick()