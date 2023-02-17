# Implemente una función que acepte 3 valores enteros a, b, c. La función debería devolver verdadero si se puede construir un triángulo con los lados de la longitud dada y falso en cualquier otro caso.

# ¿ que forma de lograr esto conoces  ?

def is_triangle(a, b, c):
    return (a + b) > c and (a + c) > b and (b + c) > a

## REALIZADO ## 