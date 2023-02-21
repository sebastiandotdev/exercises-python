# Los trolls están atacando la sección de comentarios!

# Una forma común de lidiar con esta situación es eliminar todas las vocales de los comentarios de los trolls, neutralizando la amenaza.

# Tu tarea es escribir una función que tome una cadena de texto y devuelva una nueva cadena de texto con todas las vocales eliminadas.

# Por ejemplo, la cadena "¡Este sitio web es para perdedores jaja!" se convertiría en "Est st wb s fr prddrs jh!".

# Nota: para este problema, la letra "y" no se considera una vocal.

#  ¿ que forma de lograr esto conoces  ?

def disiemvomel(string_):
    vocals = ['a', 'e', 'i', 'o', 'u']
    new_string = ""
    for characters in string_:
        if characters.lower() not in vocals:
            new_string += characters
    return new_string            

## REALIZADO ##