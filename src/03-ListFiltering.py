# En este kata, creará una función que toma una lista de enteros y cadenas no negativos y devuelve una nueva lista con las cadenas filtradas.

# ¿ que forma de lograr esto conoces  ?


def filter_list(l):
    def par(num):
        return not isinstance(num, str)
    result = list(filter(par, l))
    return result

## REALIZADO ##