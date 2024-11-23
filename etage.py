from facade import facade
from random import shuffle,randint
from fenetre import fenetre
from fenetre_balcon import fenetre_balcon
import turtle

def etage(x, y_sol, couleur, niveau):
    '''
    Paramètres
        x : abscisse du centre de l'étage
        y_sol : ordonnée du sol du la rue
        couleur : couleur de la façade de l'étage
        niveau : numéro de l'étage en partant de 0 pour le rdc
    Remarque
       Cette fonction dessine un étage d'un immeuble
    '''
    # dessin des murs

    # dessin des 3 Eléments
    # facade(x, y_sol, couleur, niveau)
    # i = randint(1,2)
    # if i == 1 :
    #     fenetre(x+15,y_sol+60*niveau+15)
    # else : fenetre_balcon(x+15,y_sol+60*niveau+55)

    # i = randint(1,2)
    # if i == 1 :
    #     fenetre(x+60,y_sol+60*niveau+15)
    # else : fenetre_balcon(x+60,y_sol+60*niveau+55)
    
    # i = randint(1,2)
    # if i == 1 :
    #     fenetre(x+105,y_sol+60*niveau+15)
    # else : fenetre_balcon(x+105,y_sol+60*niveau+55)
    
    
    facade(x, y_sol, couleur, niveau)

    # Coordinates for the windows or balconies
    positions = [15, 60, 105]

    for pos in positions:
        i = randint(1, 2)
        if i == 1:
            fenetre(x + pos, y_sol + 60 * niveau + 15)
        else:
            fenetre_balcon(x + pos, y_sol + 60 * niveau + 55)

        
    

if __name__ == '__main__':
    etage(0,0,"red",0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()