import turtle
from trait import trait

def toit2(x, y_sol, niveau):
    '''
    Paramètres :
        x : abcisse du centre du toit
        y_sol : ordonnée du sol du la rue
        niveau : num du niveau (0 pour les rdc, ...)
    Cette fonction dessine un toit plat d'épaisseur 10 pixels et mesurant 140 pixels de large
    '''
    
    epaisseur = 10
    offset = epaisseur / 2
    
    turtle.up()
    turtle.pensize(epaisseur)
    
    y_sol += 60 * niveau
    turtle.goto(x,y_sol+offset)
    
    turtle.down()
    
    turtle.pencolor('black')
    turtle.forward(140)
    
    # Retour à la taille normale
    turtle.pensize(1)
    

if __name__ == '__main__':
    toit2(0,0,0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()