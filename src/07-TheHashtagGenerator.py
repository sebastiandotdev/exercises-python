# # El equipo de marketing dedica demasiado tiempo a escribir hashtags.
# ¡Ayudémoslos con nuestro propio Generador de Hashtags!

# Aquí está el trato:

# Debe comenzar con un hashtag (#).
# Todas las palabras deben tener su primera letra en mayúscula.
# Si el resultado final tiene más de 140 caracteres, debe devolver falso.
# Si la entrada o el resultado es una cadena vacía, debe devolver falso.

#  ¿ que forma de lograr esto conoces  ?

def generate__hasgtag(string: str):
    """Generate hasgtag. """
    if not string:
        return False
    array__string = string.split()
    generate__string = [word.capitalize() for word in array__string]
    string__join = '#' + ''.join(generate__string)

    if len(string__join) > 140:
        return False
    return string__join

## REALIZADO ##