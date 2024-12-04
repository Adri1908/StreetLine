from turtle import Turtle, Screen
import math

def interpolate_color(color1, color2, t):
    """
    Interpole entre deux couleurs en fonction du facteur t (0 <= t <= 1).
    """
    c1 = tuple(int(color1[i:i+2], 16) for i in (1, 3, 5))  # Convertir en RGB
    c2 = tuple(int(color2[i:i+2], 16) for i in (1, 3, 5))
    result = tuple(int(c1[i] + (c2[i] - c1[i]) * t) for i in range(3))
    return f"#{result[0]:02x}{result[1]:02x}{result[2]:02x}"  # Retourner en format hex

def draw_gradient(t, x, y, max_radius, gradient_colors, steps):
    """
    Dessine un dégradé fluide en cercles concentriques.
    """
    for i in range(steps):
        # Calculer la couleur interpolée
        t_factor = i / (steps - 1)
        segment_index = min(int(t_factor * (len(gradient_colors) - 1)), len(gradient_colors) - 2)
        local_t = (t_factor * (len(gradient_colors) - 1)) % 1
        color = interpolate_color(gradient_colors[segment_index], gradient_colors[segment_index + 1], local_t)
        
        # Calculer le rayon du cercle
        radius = max_radius - (i * max_radius / steps)
        
        # Dessiner le cercle
        t.penup()
        t.goto(x, y - radius)
        t.pendown()
        t.color(color)
        t.begin_fill()
        t.circle(radius)
        t.end_fill()

def draw_astre(t, x, y, size, is_day):
    """
    Dessine l'astre (soleil ou lune) à la position donnée.
    
    Arguments :
    t : turtle.Turtle - Instance de la tortue pour dessiner
    x, y : float - Position de l'astre
    size : float - Taille de l'astre
    is_day : bool - Indique s'il s'agit du jour (True) ou de la nuit (False)
    """
    
    astre_color = "yellow" if is_day else "white"
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.color(astre_color)
    t.begin_fill()
    t.circle(size)
    t.end_fill()
    
    t.color("black")
    

def ciel(t, hour):
    """
    Fonction pour dessiner un ciel en fonction de l'heure donnée.

    Arguments :
    t : turtle.Turtle - Instance de la tortue pour dessiner
    hour : int - Heure de la journée (0-23)
    """
    screen = t.getscreen()
    screen_width = screen.window_width()
    screen_height = screen.window_height()
    
    screen.tracer(0)

    custom_origin_x = -screen_width // 2
    custom_origin_y = -screen_height // 2

    if 6 <= hour <= 19:
        is_day = True
    else:
        is_day = False

    is_sunrise = (6 <= hour <= 8)       # lever de soleil
    is_sunset = (16 <= hour <= 19)      # coucher de soleil

    background_color = "lightblue" if is_day else "darkblue"
    
    arc_radius = screen_width // 2
    angle = (hour - 6) / 12 * 180 if is_day else (hour - 18) / 12 * 180
    x_astre = custom_origin_x + screen_width // 2 + arc_radius * math.cos(math.radians(angle))
    y_astre = custom_origin_y + arc_radius * math.sin(math.radians(angle))

    if not is_sunrise and not is_sunset:
        screen.bgcolor(background_color)
    else:
        gradient_colors = ["#FF4500", "#FFA500", "#FFD700", "#87CEEB"] if is_sunrise else ["#87CEEB", "#FFD700", "#FFA500", "#FF4500"]
        draw_gradient(t, x_astre, y_astre, screen_width * 1.4, gradient_colors, 100)
    
    # Dessiner l'astre
    draw_astre(t, x_astre, y_astre-60, 60, is_day)
    
    screen.update()
    screen.tracer(1)


if __name__ == "__main__":
    t = Turtle()
    t.speed(0)
    t.hideturtle()
    ciel(t, 7)  # Par exemple, lever de soleil à 7h
    Screen().mainloop()
