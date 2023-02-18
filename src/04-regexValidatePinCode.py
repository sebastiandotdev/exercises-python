# Las máquinas de cajeros automáticos (ATM) permiten códigos PIN de 4 o 6 dígitos y los códigos PIN no pueden contener nada más que exactamente 4 dígitos o exactamente 6 dígitos.

# Si se le pasa a la función una cadena de texto válida como PIN, devolverá verdadero (true), de lo contrario devolverá...

# ¿ que forma de lograr esto conoces  ?

def validate_pin(pin):
    if len(pin) == 4 or len(pin) == 6:
        if pin.isdigit():
            return True
    return False

## REALIZADO ## 