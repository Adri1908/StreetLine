import turtle

def trait(x1,y1,x2,y2):
    '''
    Paramètres
        x1, y1 : coordonnées du début du trait
        x2, y2 : coordonnées de la fin du trait
    Cette function dessine un trait entre les 2 points transmis en paramètres
    '''
<<<<<<< HEAD
    turtle.up()
    turtle.goto(x1,y1)
    turtle.down()
    turtle.goto(x2,y2)
    turtle.up()
=======
    print("test 100")
#KILIAN PUE LA GROSSE MERD*

>>>>>>> cdcb0850c33234d49ded58f855c9a52ce998f0c7
if __name__ == '__main__':
    trait(0,0,100,100)
    
    # On ferme la fenêtre s'il y a un clique gauche
    #essai
    turtle.exitonclick()