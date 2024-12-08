import turtle
from random import randint, shuffle
from rectangle import rectangle
from sol import sol
from ciel import ciel
from immeuble import immeuble

def main():
    turtle.setup(800, 600)
    turtle.speed(0)
    
    # Hauteur du sol
    y_sol = -200

    # Création du ciel
    ciel(turtle, randint(0, 23))
    
    # Dessin du sol de la rue
    sol(y_sol)
    
    # Remplissage du sol
    screen = turtle.getscreen() # Taille de l'écran
    
    turtle.fillcolor("black")   # Change la couleur de remplissage
    turtle.begin_fill()         # Précise le début du remplissage
    
    rectangle(-(screen.window_width()//2),          # coordonnée X du centre de la base
              -(screen.window_height()//2),         # coordonnée Y du centre de la base
              screen.window_width(),                # largeur
              abs(y_sol)//2)                        # hauteur    
    
    turtle.end_fill()           # Fin du remplissage 
    
    # Dessin des immeubles
    for i in range(4):
        immeuble(-320+i*180, y_sol)

    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()
    
if __name__ == '__main__':
    main()



