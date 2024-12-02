import turtle
import math

def toit1(x, y_sol, niveau):
    '''
    Paramètres :
        x : abcisse du centre du toit
        y_sol : ordonnée du sol du la rue
        niveau : num du niveau (0 pour les rdc, ...)
    Cette fonction dessine un toit triangulaire noir de base 160 pixels
    et de hauteur centrale 40 pixels
    '''
    # Dimensions du toit
    largeur_base = 160
    offset = 10
    hauteur = 40
    demi_base = largeur_base / 2
    hypotenuse = math.sqrt((demi_base)**2 + hauteur**2)
    angle_base_vers_côté = math.degrees(math.atan(hauteur / demi_base))
    
    # Calculer la coordonnée y pour le niveau actuel
    y = y_sol + 60 * niveau
    
    # Se déplacer au point de départ (coin gauche de la base - offset)
    turtle.up()
    turtle.goto(x-offset, y)
    turtle.down()
    
    # Dessiner le toit
    turtle.fillcolor('black')
    turtle.begin_fill()
    
    # Base du toit
    turtle.forward(largeur_base)
    
    # Côté gauche du triangle
    turtle.left(180 - angle_base_vers_côté)
    turtle.forward(hypotenuse)
    
    # Côté droit du triangle
    turtle.left(2 * angle_base_vers_côté)
    turtle.forward(hypotenuse)
    
    # Retourner à la base
    turtle.left(180 - angle_base_vers_côté)
    turtle.end_fill()

if __name__ == '__main__':
    toit1(0, 0, 0)
    # Fermer la fenêtre avec un clic gauche
    turtle.exitonclick()
