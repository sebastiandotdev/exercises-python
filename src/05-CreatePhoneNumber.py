# Escriba una función que acepte una matriz de 10 enteros (entre 0 y 9), que devuelva una cadena de esos números en forma de número de teléfono.


#  ¿ que forma de lograr esto conoces  ?

def create_phone_number(n):
    phone__number = "".join(map(str, n))
    return print('({}{}{}) {}{}{} - {}{}{}{}'.format(*phone__number))
    

## REALIZADO ##
