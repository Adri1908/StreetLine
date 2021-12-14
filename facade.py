import turtle
from rectangle import rectangle

def facade(x, y_sol, couleur, niveau):
    '''
    Paramètres :
        x : abcisse du centre de la façade
        y_sol : ordonnée du sol du la rue
        couleur : couleur de la façade
        niveau : num du niveau (0 pour les rdc, ...)
    remarque :
        Facade dessine une facade sans les élements interieurs
    '''
<<<<<<< HEAD
    turtle.fillcolor("red")
    turtle.begin_fill()
    rectangle(x, y_sol, 140, 60)
    turtle.end_fill()
=======

    turtle.fillcolor(couleur)  #Change la couleur de remplissage à rouge
    turtle.begin_fill()  #Précise le début du remplissage
    rectangle(x,y_sol + 60 * niveau,140,60)
    turtle.end_fill() 
>>>>>>> 8ac6a85baa0f0c59e9a1d3bffdcaf500e9634053






if __name__ == '__main__':
    facade(0,0,"red",0)
    # On ferme la fenêtre s'il y a un clique gauche
    turtle.exitonclick()