import random

from facade import facade
from random import shuffle
from porte import porte
from porte2 import porte2
from fenetre import fenetre
from random import randint
import turtle

def rdc(x, y_sol, couleur_facade, couleur_porte):
    '''
    Paramètres
        x : (int) abscisse du centre
        y_sol : ordonnée du sol du la rue
        c_facade : couleur de la façade
        c_porte : couleur de la porte
    remarque:
        Cette fonction dessine le rdc en 2 étapes
        D'abord la façade
        Puis les 3 élements : 1 porte et 2 fenêtres disposées au hasard
    '''
    # Dessine la facade
    facade(x, y_sol, couleur_facade, 0)

    # Coordonnées des positions des 3 éléments
    positions = [10, 55, 100]

    # Construit les 3 éléments (1 porte et 2 fenetres)
    pos = randint(0, 2)
    for i in range(len(positions)):
        if i == pos:
            (random.choice([porte, porte2]))(x + positions[i], y_sol, couleur_porte)
        else:
            fenetre(x + positions[i], y_sol + 20)


if __name__ == '__main__':
    rdc(0,0,"red","green")
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()