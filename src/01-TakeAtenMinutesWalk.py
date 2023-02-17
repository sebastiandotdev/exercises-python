# Vives en la ciudad de Cartesia, donde todos los caminos están dispuestos en una cuadrícula perfecta. Llegaste diez minutos antes a una cita, por lo que decidiste aprovechar para dar un pequeño paseo. La ciudad proporciona a sus ciudadanos una aplicación de generación de caminatas en sus teléfonos: cada vez que presiona el botón, le envía una serie de cadenas de una letra que representan las direcciones para caminar (por ejemplo, ['n', 's', 'w', 'mi']). Siempre camina solo una cuadra por cada letra (dirección) y sabe que le toma un minuto atravesar una cuadra de la ciudad, así que cree una función que se vuelva verdadera si la caminata que le da la aplicación le toma exactamente diez minutos (usted ¡No quiero llegar temprano ni tarde!) y, por supuesto, lo regresará a su punto de partida. Devuelve false en caso contrario.

# Nota: siempre recibirá una matriz válida que contenga una variedad aleatoria de letras de dirección (solo 'n', 's', 'e' o 'w'). Nunca le dará una matriz vacía (¡eso no es caminar, eso es quedarse quieto!).

# ¿ que forma de lograr esto conoces  ?

def is_valid_walk(walk):
    if len(walk) != 10:
        return False
    
    x = y = 0
    for direction in walk:
        if direction == 'n':
            y += 1
        elif direction == 's':
            y -= 1
        elif direction == 'e':
            x += 1
        elif direction == 'w':
            x -= 1
    return x == y == 0

## REALIZADO ##
